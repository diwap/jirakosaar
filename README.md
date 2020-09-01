# Jirakosaar
![python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue) ![pylint](https://img.shields.io/badge/pylint-9.71-brightgreen)  
Jirakosaar is a command line tool to get summary of jira issues.

## Installation and Setup
```bash
python3 -m pip install --user jirakosaar
```
After installing, we need to configure basic authentication. Before setting up, we need to create [API Token](https://id.atlassian.com/manage-profile/security/api-tokens) from Jira.

Guide for Cloud: [https://confluence.atlassian.com/cloud/api-tokens-938839638.html](https://confluence.atlassian.com/cloud/api-tokens-938839638.html)

We will set email and token as password for basic authentication.

In terminal run below command to configure credential:
```
jirakosaar configure
```
__Output Sample__
```
Email: test@example.com
API_TOKEN: 123456

Configuring credential completed
```

This will create `config.json` file in `$HOME/.jirakosaar` directory.

### Linux
Might need to export path for some Linux distribution. To set it permanently, export in `~/.bash_profile`.
```
export PATH=$PATH:~/.local/bin
```

### MacOS
Need to export path. To set it permanently, export in `~/.bash_profile`.
```
export PATH=$PATH:~/Library/Python/3.*/bin
```

## Usage
```
jirakosaar [args]

Available arguments

active      List Completed and Incomplete issues of active sprint
backlog     List all issues of backlog
configure   Prompt for setting up credentials of Jira API
```

## Package File Structure
```
jirakosaar
├── __init__.py
├── config
│   ├── __init__.py
│   └── configure.py
└── issues
    ├── __init__.py
    ├── auth
    │   ├── __init__.py
    │   └── auth.py
    └── main.py
```

## Reason to create this tool
Whenever I had to go through sprint review, I have to manually copy issue summary and paste in presentation document. I felt pretty boring to do that everytime. If I get summary in cli then the thing left to do is just copy and paste from the stdout.

With this package, don't expect to get big but pretty helpful to lazy people like me.


## Contributions
Any kind of contribution and issue reporting is heartily welcome. However, it should pass pylint linting tool rating. Aim should be 10/10. There might be exception which can be considered if admin accept. TODO comment are exceptional case.
