import sys
import math
from collections import defaultdict


def main():
    k = int(sys.stdin.readline().strip())
    for i in range(k):
        n = int(sys.stdin.readline().strip())
        # {stamp: [owners]}
        owners_map = defaultdict(set)
        for j in range(n):
            stamps = list(map(int, sys.stdin.readline().strip().split()[1:]))
            for stamp in stamps:
                owners_map[stamp].add(j)
 
        # build reverse mapping {owner: stamps}
        # ignoring stamps with multiple owners
        owners = [0] * n
        for owners_list in owners_map.values():
            if len(owners_list) == 1:
                owners[owners_list.pop()] += 1

        distinct = sum(owners)
        out = " ".join([f"{owned/distinct * 100:.6f}%" for owned in owners])
        print(f"Case {i+1}: {out}")


if __name__ == "__main__":
    main()
