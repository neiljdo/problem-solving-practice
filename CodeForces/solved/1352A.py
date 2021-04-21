import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    summands = []
    mult = 1
    while n:
        digit = n % 10
        if digit:
            summands.append(str(digit * mult))
        n //= 10
        mult *= 10

    print(len(summands))
    print(" ".join(summands))
