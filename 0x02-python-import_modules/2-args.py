#!/usr/bin/python3
from this import d


if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv
    count = 1

    number_of_args = len(argv) - 1
    if number_of_args == 0:
        print(f"{number_of_args:d} arguments.")
    if number_of_args == 1:
        print(f"{number_of_args:d} arguments.")
    if number_of_args > 1:
        print(f"{number_of_args:d} arguments.")
    while count < len(argv):
        print(f"{count:d}: {argv[count]}")
        count += 1
