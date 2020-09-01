import sys
import math
from functools import partial


"""
Implemnet method that take a string representing an integer and return the corresponding
integer, and vice versa. Must handle negative integers. Library functions like `int` are
not allowed.
"""


def string_to_int(s):
    # check if negative
    is_negative = False
    if s[0] == "-":
        is_negative, s = True, s[1:]
    result = 0
    # O(len(s)) time, O(1) space
    while s:
        result += ord(s[0]) - ord('0')
        s = s[1:]
        if s:
            result *= 10
    if is_negative: result *= -1
    return result

def int_to_string(i):
    result = ""
    is_negative = False
    if i < 0:
        is_negative, i = True, -i
    # reversed result
    if i == 0: return "0"
    while i:
        result += chr(ord('0') + (i % 10))
        i //= 10
    if is_negative:
        result += "-"
    return ''.join(reversed(result))


if __name__ == "__main__":
    print(string_to_int("0"))
    print(string_to_int("2"))
    print(string_to_int("-9"))
    print(string_to_int("23456"))
    print(string_to_int("-23456"))

    print(int_to_string(0))
    print(int_to_string(2))
    print(int_to_string(-9))
    print(int_to_string(23456))
    print(int_to_string(-23456))
