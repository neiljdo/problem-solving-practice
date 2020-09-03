import sys
import math
from functools import partial


def main():
    while 1:
        s, b = list(map(int, sys.stdin.readline().strip().split()))
        if not s and not b: break
        # O(n + b)
        next_el = list(range(1, s+1))
        next_el.append(None)
        prev_el = [None]
        for i in range(s): prev_el.append(i)
        
        for _ in range(b):
            l, r = list(map(int, sys.stdin.readline().strip().split()))

            L, R = prev_el[l], next_el[r]

            out_l = "*" if not L else L
            out_r = "*" if not R else R
            print(out_l, out_r)
            if L is not None:
                next_el[L] = R
            if R is not None:
                prev_el[R] = L

        print("-")

if __name__ == "__main__":
    main()
