import sys
import math


def main():
    while 1:
        line = sys.stdin.readline()
        if not line: break
        line = line.strip()
        if not line: continue

        n = int(line)
        prices = list(map(int, sys.stdin.readline().strip().split()))
        m = int(sys.stdin.readline().strip())

        i, j = -1, -1

        seen = set()
        min_price_diff = math.inf
        for p in prices:
            if p != m:
                complement = m - p
                if p in seen:
                    price_diff = abs(complement - p)
                    if price_diff < min_price_diff:
                        min_price_diff = price_diff
                        i, j = p, complement
                else:
                    seen.add(complement)

        if j < i:
            i, j = j, i
        
        print(f"Peter should buy books whose prices are {i} and {j}.\n")


if __name__ == "__main__":
    main()
