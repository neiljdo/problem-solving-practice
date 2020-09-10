import sys
import math
from collections import OrderedDict


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        cs = list(map(int, sys.stdin.readline().strip().split()[1:]))
        running_total = 1
        collection_count = 1
        for i, c in enumerate(cs[:-1]):
            running_total += c
            if running_total < cs[i+1]:
                collection_count += 1
            else:
                # don't include c
                running_total -= c
        
        print(collection_count+1)
        

if __name__ == "__main__":
    main()
