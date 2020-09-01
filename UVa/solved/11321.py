import sys
import math
from functools import partial


class Sortable:
    def __init__(self, val=None, m=None):
        self.val = val
        self.m = m

    def mod_m(self):
        mod = self.val % self.m
        if self.val < 0 and mod != 0:
            mod -= self.m
        return mod

    def __lt__(self, other):
        if self.mod_m() == other.mod_m():
            if self.val % 2 == 0 and other.val % 2 == 0:
                return self.val < other.val
            elif self.val % 2 == 1 and other.val % 2 == 1:
                return self.val > other.val
            else:
                return self.val % 2 == 1
        else:   
            return self.mod_m() < other.mod_m()


def main():
    while True:
        n, m = list(map(int, sys.stdin.readline().strip().split()))
        print(n, m)
        if not (n or m): break
        sortables = []
        for i in range(n):
            sortables.append(Sortable(val=int(sys.stdin.readline().strip()), m=m))
        sortables.sort()
        for sortable in sortables:
            print(sortable.val)


if __name__ == "__main__":
    main()
