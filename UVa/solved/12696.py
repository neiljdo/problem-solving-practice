import sys
import math


def main():
    t = int(sys.stdin.readline())
    valid_cnt = 0
    for t in range(t):
        l, w, d, wt = list(map(float, sys.stdin.readline().strip().split()))
        valid = int(
            wt <= 7. and
            ((l <= 56. and w <= 45. and d <= 25.) or l+w+d <= 125.)
        )
        print(valid)
        valid_cnt += valid
    print(valid_cnt)


if __name__ == "__main__":
    main()
