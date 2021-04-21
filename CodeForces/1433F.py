import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    piranhas = list(map(int, sys.stdin.readline().strip().split()))

    maxPiranha = max(piranhas)
    ind = -2
    for i, p in enumerate(piranhas):
        if p == maxPiranha:
            if i == 0:
                if piranhas[i+1] < maxPiranha:
                    ind = i
                    break
            elif i == len(piranhas) - 1:
                if piranhas[i-1] < maxPiranha:
                    ind = i
                    break
            elif piranhas[i-1] < maxPiranha or piranhas[i+1] < maxPiranha:
                ind = i
                break
    print(ind+1)