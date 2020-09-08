import sys


n = int(sys.stdin.readline().strip())
if n % 2 == 0:
    print(2 ** (n // 2))
else:
    print(0)
