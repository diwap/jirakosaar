"""configure module create directory in home path and intialize config file
taking input from user. This create a json file and use `json` package to
load and dump file.
"""

import os
import json


# TODO Make this func dynamic to handle different auth and probably logic in auth itself.
def get_input_data(prev_data):
    """Take input from user to set email and api_token in config file.
    """
    try:
        if prev_data:
            return {
                "email": str(input(f"Email({prev_data.get('email')}): ")) \
                    or prev_data.get('email'),
                "api_token": str(input(f"API_TOKEN({prev_data.get('api_token')}): ")) \
                    or prev_data.get('api_token')
            }
        return {
            "email": str(input("Email: ")),
            "api_token": str(input("API_TOKEN: "))
        }
    except KeyboardInterrupt:
        print("\n\nInterrupted! Using previous config if exists")

class Configure:
    """Class needs to import and initialized with config_dir args.
    Basic implementation of Configure class::

        >>> from jirakosaar.config.configure import Configure

        >>> config = Configure("/path/to/file")
        >>> config.set_credential()
    """

    def __init__(self, config_dir: str):
        self.config_dir = config_dir
        self.config_file = os.path.join(self.config_dir, "config.json")

    def get_credential(self):
        """Read config file and read file with readonly permission then
        return data using `json.loads` function.
        """
        try:
            with open(self.config_file, "r") as file:
                return json.loads(file.read())
        except json.decoder.JSONDecodeError:
            pass
        except FileNotFoundError:
            pass

    def set_credential(self):
        """Create dir if doesn't exists. Check for old credential, if
        exists same will be set if input not provided. If input provided,
        old value will be replaced with new one. Any empty input will ask to
        provide input again. Final data is dumped in a json format with
        the indentation of 4.
        """

        try:
            os.mkdir(self.config_dir)
        except FileExistsError:
            pass

        old_cred = self.get_credential()

        with open(self.config_file, "w") as file:
            data = get_input_data(old_cred)

            while not (data.get("email") and data.get("api_token")):
                print("\nNeed both input\n")
                data = get_input_data(old_cred)

            json_obj = json.dumps(data or old_cred, indent=4)

            file.write(json_obj)
            file.write("\n")

            if data:
                print("\nConfiguring credential completed")
