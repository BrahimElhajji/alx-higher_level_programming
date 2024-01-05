#!/usr/bin/python3
import sys
if __name__ == "__main__":

    argc = len(sys.argv) - 1

    if argc == 0:
        print(f"{argc:d} arguments.")
    elif argc == 1:
        print(f"{argc:d} argument:")
    else:
        print(f"{argc:d} arguments:")

    if argc >= 1:
        argc = 0
        for ar in sys.argv:
            if argc != 0:
                print(f"{argc:d}: {ar:s}")
            argc += 1
