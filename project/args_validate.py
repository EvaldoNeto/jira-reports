"""
Model with function to validate the args
"""

import sys

def validate_args(args):
    """
    Function to validate the args
    """
    if len(args) == 2:
        try:
            args = int(args[1])
        except ValueError:
            print(f"Error: wrong argument {args[1]}, it should be an integer")
            sys.exit()
    else:
        print("Error: wrong number of arguments, it should just have one")
        sys.exit()
