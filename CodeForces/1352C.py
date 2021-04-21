import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    
    # 3, 15
    ordinal, last = 0, 0
    while ordinal < k:
        numDivisible = (k - ordinal) // n # 5 // 3 = 1
        if numDivisible == 0:
            last += k - ordinal
            break
        else:
            last += numDivisible * n
            ordinal = k - numDivisible # 15,10

    print(last)
    