import sys
import math
from functools import partial


"""
Compute the parity of a large number of 2 ** 64 integers.

e.g.
 9 -> 1001 -> 0
11 -> 1011 -> 1
"""

def parity_naive(n):
    """
    1001 & 0001 = 0001 = 1
    0 ^ 1 = 1       # xor
    0100 & 0001 = 0
    1 ^ 0 = 1
    0010 & 0001 = 0
    1 ^ 0 = 1
    0001 & 0001 = 1
    1 ^ 1 = 0
    """
    parity = 0
    while n:
        parity ^= n & 1
        n >>= 1
    return parity


def main():


if __name__ == "__main__":
    main()
