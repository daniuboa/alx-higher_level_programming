#!/usr/bin/python3

if __name__ == "__main__":
<<<<<<< HEAD
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

    print(f"{total}")
=======
    from sys import argv

    total = 0
    for i in range(len(argv) - 1):
        total += int(argv[i + 1])

    print(f"total")
>>>>>>> 22b61288cde4391e060b5cef42a1d50039f2265b
