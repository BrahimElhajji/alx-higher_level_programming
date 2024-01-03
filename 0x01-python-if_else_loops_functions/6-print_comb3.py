#!/usr/bin/python3
for n in range(0, 10):
    for i in range(n + 1, 10):
        if n == 8 and i == 9:
            print('89')
        else:
            print('{:d}{:d}, '.format(n, i), end='')
