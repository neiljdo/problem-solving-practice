import sys


n = int(sys.stdin.readline().strip())
w = 0
for i in range(2, n):
    w += i * (i+1)

print(w)
