import sys
import math
from functools import partial


def main():
    def get_price(a, b, c, d, k):
        return math.sin(a * k + b) + math.cos(c * k + d)

    for line in sys.stdin:
        p, a, b, c, d, n = list(map(int, line.strip().split()))
        price_k = partial(get_price, a, b, c, d)
        prices = [price_k(i+1) for i in range(n)]

        max_price = -math.inf
        max_decline = math.inf
        for price in prices:
            max_price = max(max_price, price)
            max_decline = min(max_decline, price - max_price)
        print(p * abs(max_decline))

if __name__ == "__main__":
    main()
