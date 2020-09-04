import sys
import math
import sortedcontainers


def transform(g):
    out = [r[:] for r in g]
    # print(g)
    for r in range(3):
        for c in range(3):
            left = 0 if c - 1 < 0 else g[r][c-1]
            top = 0 if r - 1 < 0 else g[r-1][c]
            right = 0 if c + 1 > 2 else g[r][c+1]
            bottom = 0 if r + 1 > 2 else g[r+1][c]

            out[r][c] = (top + bottom + left + right) % 2
            # print(top, bottom, left, right)
            # print(f"out[{r}][{c}] = {out[r][c]}")

    return out

import time
def main():
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        k = -1
        _ = sys.stdin.readline()
        g = [
            list(map(int, list(sys.stdin.readline().strip()))) for i in range(3)
        ]
        while any([any(r) for r in g]):
            k += 1
            g = transform(g)
            # gstr = "\n".join(["".join([str(e) for e in r]) for r in g])
            # print(f"will continue?\n{gstr} - {any([any(r) for r in g])}")
        print(k)

if __name__ == "__main__":
    main()
