import sys
import math
from collections import defaultdict


def main():
    while True:
        days = int(sys.stdin.readline().strip())
        if not days: break
        total = 0
        urn = defaultdict(int)
        for _ in range(days):
            bills = list(map(int, sys.stdin.readline().strip().split()[1:]))
            for bill in bills:
                urn[bill] += 1
            # simulate raffle
            # TODO: cache min and max for O(1) lookup
            distinct_bills = sorted(urn.keys())
            min_bill, max_bill = distinct_bills[0], distinct_bills[-1]
            total += max_bill - min_bill
            urn[max_bill] -= 1
            if urn[max_bill] <= 0: del urn[max_bill]
            urn[min_bill] -= 1
            if urn[min_bill] <= 0: del urn[min_bill]
        print(total)


if __name__ == "__main__":
    main()
