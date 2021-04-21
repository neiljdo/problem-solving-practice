import sys
import math
import heapq
from collections import defaultdict


def main():
    while True:
        days = int(sys.stdin.readline().strip())
        if not days: break
        total = 0
        min_heap = []
        max_heap = []
        for _ in range(days):
            bills = list(map(int, sys.stdin.readline().strip().split()[1:]))
            for bill in bills:
                heapq.heappush(min_heap, bill)
                heapq.heappush(max_heap, -bill)

            max_bill = -heapq.heappop(max_heap)
            min_bill = heapq.heappop(min_heap)
            if len(min_heap) == 1 and len(max_heap) == 1:
                heapq.heappop(max_heap)
                heapq.heappop(min_heap)
            total += max_bill - min_bill
        print(total)


if __name__ == "__main__":
    main()
