import sys
import math
from collections import OrderedDict


def main():
    t = 0
    while True:
        n, d = list(map(int, sys.stdin.readline().strip()))
        if not n and not d: break
        t += 1
        islands = []
        impossible = False
        for _ in range(n):
            island = list(map(int, sys.stdin.readline().strip()))
            impossible = impossible or island[1] > d
            islands.append(list(map(int, sys.stdin.readline().strip())))
        sys.stdin.readline().strip()

        if impossible:
            print(f"Case {t}: -1")
        else:
            pass
        

if __name__ == "__main__":
    main()
