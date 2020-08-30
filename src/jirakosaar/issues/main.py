"""main module include `Issues` class to handle jira requests and print data in stdout.
"""

import os
import sys
import json

import requests

from jirakosaar.issues.auth.auth import BasicAuthentication


BASE_URL = "https://uxcamcom.atlassian.net/rest/api/3"


def parse_issues(issues: list) -> list:
    """Get key, summary and labels which is created as a statement.
    Output Sample
    -------------
        [
            {
                "is_completed": True,
                "statement": "ENG-1 : Create sprint ticket [backend]"
            }
        ]
    """

    data = []
    for item in issues:
        # TODO add tag newly_created automatically matching sprint started date and issue date
        # eg. created_date = i.get('fields').get('created') # to get [newly created] tag
        labels = ' '.join(f"[{item}]" for item in item.get('fields').get('labels'))

        def is_completed():
            if not item.get('fields').get('status').get('name') == 'Done':
                return False
            return True

        data.append({
            "is_completed": is_completed(),
            "statement": f"{item.get('key')} : {item.get('fields').get('summary')} {labels}"
        })
    return data


class Issues:
    """Search config, requets in the api endpoint and parse response. Reponse is then stdout
    in the terminal.
    Usage Example
    ----------
        >>> from jirakosaar.issues.main import Issues

        >>> issues = Issues("path/to/config")
        >>> issues.get_backlog_issues()
    """
    def __init__(self, config_dir: str):
        self.config_dir = config_dir
        self.config_file = os.path.join(self.config_dir, "config.json")

    def __get_auth_config(self) -> dict:
        try:
            with open(self.config_file, "r") as file:
                data = json.loads(file.read())
                return data
        except FileNotFoundError:
            print(f"Configuration file not found!\nNeed {self.config_file}")
            sys.exit()
        sys.exit()

    def get_response(self, jql: str) -> dict:
        """Create request endpoint with necessary headers and params, then send
        request and return response as a `dict`.
        Example
        --------
            >>> jql = 'resolution = "Done"'
            >>> get_response(jql)
        """

        basic_auth = BasicAuthentication(self.__get_auth_config())
        data = {
            "headers": {"Accept": "application/json"},
            "auth": basic_auth(),
            "params": {'jql': jql}
        }

        response = requests.request(
            "GET",
            f"{BASE_URL}/search",
            **data
        )

        if response.status_code != '200':
            sys.exit("\nI could not get 200 success status! \
                \nPlease check your auth credential or internet.")

        return json.loads(response.text).get('issues')

    def get_current_issues(self):
        """Stdout issues of authenticated user of open sprint.
        """

        jql = 'Sprint in openSprints() AND assignee = currentUser() ORDER BY updatedDate DESC'
        print("Completed\n=============")
        for item in parse_issues(self.get_response(jql)):
            if item.get('is_completed'):
                print(item.get('statement'))

        print("\nNot Completed\n=============")
        for item in parse_issues(self.get_response(jql)):
            if not item.get('is_completed'):
                print(item.get('statement'))

    def get_backlog_issues(self):
        """Stdout issues of authenticated user whose sprint is empty and unresolved.
        """

        jql = 'Sprint is EMPTY AND assignee = currentUser() \
            AND resolution = Unresolved ORDER BY updated DESC'
        print("Backlog\n=============")
        for item in parse_issues(self.get_response(jql)):
            print(item.get('statement'))
        print("\n")
