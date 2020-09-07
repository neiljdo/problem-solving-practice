import sys
from collections import Counter


n = sys.stdin.readline()
bars = Counter(list(map(int, sys.stdin.readline().strip().split())))

print(bars.most_common()[0][1], len(bars.keys()))
