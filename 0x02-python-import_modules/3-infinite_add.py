#!/usr/bin/python3
from ast import add
from audioop import add

if __name__ == "__main__":
<<<<<<< HEAD

=======
<<<<<<< HEAD
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

    print(f"{total}")
=======
>>>>>>> 72209289b2beb530fec0da42b46bbc2f6874ff32
    from sys import argv
    addition = 0

    number_of_args = len(argv)

<<<<<<< HEAD
    if number_of_args == 0:
        print(f"{addition}")
    for argument in argv:
        if argument != argv[0]:
            addition += int(argument)
=======
    print(f"total")
>>>>>>> 22b61288cde4391e060b5cef42a1d50039f2265b
>>>>>>> 72209289b2beb530fec0da42b46bbc2f6874ff32
