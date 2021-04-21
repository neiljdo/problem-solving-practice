import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    
    summands = []
    if n == k:
        print("YES")
        print(" ".join(["1" for _ in range(n)]))
    elif n % 2 == 0:
        ncopy = n
        for _ in range(k-1):
            summands.append(2)
            ncopy -= 2
        
        if ncopy <= 0 or n % 2 == 1:
            # try odd
            summands = []
            for _ in range(k-1):
                summands.append(1)
                n -= 1

            if n <= 0 or n % 2 == 0:
                print("NO")
            else:
                print("YES")
                summands.append(n)
                print(" ".join([str(x) for x in summands]))
        else:
            print("YES")
            summands.append(ncopy)
            print(" ".join([str(x) for x in summands]))
    else:
        if k % 2 == 0:
            print("NO")
        else:
            for _ in range(k-1):
                summands.append(1)
                n -= 1
            if n <= 0 or n % 2 == 0:
                print("NO")
            else:
                print("YES")
                summands.append(n)
                print(" ".join([str(x) for x in summands]))
