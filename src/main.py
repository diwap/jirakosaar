"""Jirakosaar main module for handling arguments received while executing
command. This configure default directory and handle second index of argument.
"""

import sys
from os.path import join as join_path
from os import getenv

from jirakosaar.config.configure import Configure
from jirakosaar.issues.main import Issues


# Get home path and set default directory
CONFIG_DIR = join_path(getenv("HOME"), ".jira_config")


def main(argv):
    """Check second index from passed argument and if matches with the
    condition, returns accordingly. If not, return default message and
    exit.
    """
    default = "Avaialble args:\nactive, backlog, configure"

    if not argv:
        print(default)
        sys.exit()

    if argv[0] == 'active':
        issues = Issues(CONFIG_DIR)
        issues.get_current_issues()
        sys.exit()

    if argv[0] == 'backlog':
        issues = Issues(CONFIG_DIR)
        issues.get_backlog_issues()
        sys.exit()

    if argv[0] == 'configure':
        config = Configure(CONFIG_DIR)
        config.set_credential()
        sys.exit()

    print(default)


if __name__ == "__main__":
    main(sys.argv[1:])
