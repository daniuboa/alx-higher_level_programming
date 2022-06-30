#!/usr/bin/python3
import sys

def main():
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 arguments.")
        print(f"1. {sys.argv[1]}")
    else:
        print(f"{argc} arguments.")
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    main()
