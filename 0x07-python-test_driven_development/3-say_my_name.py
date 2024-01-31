#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints the full name based on the provided first and last names.

    Parameters:
    - first_name (str): The first name to be included in the full name.
    - last_name (str, optional): The last name to be included in the full name.
        Defaults to an empty string if not provided.

    Raises:
    - TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = "{} {}".format(first_name, last_name)
    print("My name is {}".format(full_name))
