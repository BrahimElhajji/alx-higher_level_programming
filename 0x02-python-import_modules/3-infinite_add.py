#!/usr/bin/python3
import sys

if __name__ == "__main__":
    result = 0
    for argc in range(len(sys.argv) - 1):
        result += int(sys.argv[argc + 1])
    print(result)
