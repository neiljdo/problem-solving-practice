import sys
import math
import heapq


def main():
    while True:
        k = sys.stdin().readline.strip()
        if not k: break
        k = int(k)
        k_heaps = []
        for _ in range(k):
            nums = list(map(int, sys.stdin.readline().strip().split()))
            k_heaps.append(heapq.heapify(nums))
        
        k_min_sums = []
        while len(k_min_sums) < k:
            min_sum = sum([h[0] for h in k_heaps])
            k_min_sums.append(sum)
            heapq.h

        print("".join(k_min_sums))
        
        
if __name__ == "__main__":
    main()
