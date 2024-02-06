#!/usr/bin/python3
"""class MyInt that inherits  int"""


class MyInt(int):
    "MyInt is a rebel. MyInt has == and != operators inverted"
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
