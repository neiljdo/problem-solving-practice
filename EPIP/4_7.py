import sys
import math
from functools import partial


"""
Compute x ** y.
"""

def power(base, exp):
    # O(exp) time, O(1) mem
    result = 1.
    while exp:
        result *= base
        exp -= 1
    return result

def power_v2(base, exp):
    # O(log exp), O(1) mem
    result = 1.
    while exp:
        if exp % 2:
            result *= base
        base, exp = base * base, exp // 2
    return result



if __name__ == "__main__":
    print(power(2, 5))
    print(power_v2(2, 5))
    print(power_v2(2, 4))