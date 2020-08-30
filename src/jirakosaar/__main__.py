"""Executable file when run with -m in python
"""
import os
import sys


import jirakosaar

if sys.path[0] == "" or sys.path[0] == os.getcwd():
    sys.path.pop(0)

jirakosaar.run_jirakosaar(sys.argv[1:])
