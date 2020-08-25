import sys
import math
from functools import partial


def main():
    def price(p, a, b, c, d, k):
        return p * (math.sin(a * k + b) + math.cos(c * k + d) + 2)

    for line in sys.stdin:
        p, a, b, c, d, n = list(map(int, line.strip().split()))
        price_k = partial(price, p, a, b, c, d)
        price_series = [price_k(i+1) for i in range(n)]
        p1dels = []
        # O(n)
        minp1del = 0
        minp1del_idx = 0
        for i in range(n):
            p1del = price_series[i] - price_series[0]
            if p1del < minp1del:
                minp1del = p1del
                minp1del_idx = i
            p1dels.append(p1del)

        maxp1del = max(p1dels[:minp1del_idx]) if minp1del_idx != 0 else minp1del
        max_decline = minp1del - maxp1del
        if max_decline < 0: print(abs(max_decline))
        else: print(0)


if __name__ == "__main__":
    main()
