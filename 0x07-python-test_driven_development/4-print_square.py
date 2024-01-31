#!/usr/bin/python3
def print_square(size):
    """
    Prints a square of '#' characters with a specified size.

    Parameters:
    - size (int): The size of the square.
    Must be a non-negative integer.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
