"""All authentication validation and parsing lies in this module.
"""

from requests.auth import HTTPBasicAuth


# TODO Validate email and token before initializing
class BasicAuthentication:
    """Return HTTPBasicAuth of `requests.auth` module intializing email and password.
    """
    def __init__(self, auth: dict):
        self.auth = auth

    def parse_auth(self) -> set:
        """`auth` argument is parsed to get email and password
        """
        return (self.auth.get('email'), self.auth.get('api_token'))

    def __call__(self):
        return HTTPBasicAuth(*self.parse_auth())
