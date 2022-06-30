#!/usr/bin/python3
from ast import add
from audioop import add

if __name__ == "__main__":

    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

    print(f"{total}")

    from sys import argv
    addition = 0

    number_of_args = len(argv)

    if number_of_args == 0:
        print(f"{addition}")
    for argument in argv:
        if argument != argv[0]:
            addition += int(argument)

    print(f"total")
