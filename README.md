# Jirakosaar
![python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue) ![pylint](https://img.shields.io/badge/pylint-9.67-brightgreen)  
Jirakosaar is a command line tool to get summary of jira issues.

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
