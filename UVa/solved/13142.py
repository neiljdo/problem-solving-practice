import sys
import math
from collections import OrderedDict


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        T, S, D = list(map(float, sys.stdin.readline().strip().split()))
        mass = math.floor(abs(D) * 1e4 / (T * 24 * 36))

        if D <= 0 or mass == 0:
            print(f"Add {mass} tons")
        else:
            print(f"Remove {mass} tons")
        

if __name__ == "__main__":
    main()
