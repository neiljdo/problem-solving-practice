import math
import sys


n = int(sys.stdin.readline().strip())
out, s = 1, 1

out = math.factorial(n) // (math.factorial(n // 2) ** 2)
out *= math.factorial(n // 2 - 1) ** 2
out //= 2
print(out)
