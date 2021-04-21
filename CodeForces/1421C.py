import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    x = a & b
    print((a ^ x) + (b ^ x))
