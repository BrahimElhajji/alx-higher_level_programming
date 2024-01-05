#!/usr/bin/python3
import sys
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    o = sys.argv[2]
    b = int(sys.argv[3])

    if o == '+':
        print(f"{a:d} {o:s} {b:d} = {add(a, b):d}")
    elif o == '-':
        print(f"{a:d} {o:s} {b:d} = {sub(a, b):d}")
    elif o == '*':
        print(f"{a:d} {o:s} {b:d} = {mul(a, b):d}")
    elif o == '/':
        print(f"{a:d} {o:s} {b:d} = {div(a, b):d}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
