import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    shelf = "".join(sys.stdin.readline().split())
    shelf = shelf.strip("0")
    shelf = list(map(int, [c for c in shelf]))

    start = False
    gaps = 0
    for b in shelf:
        if b == 1 and not start:
            start = True
        if b == 0 and start:
            gaps += 1
    
    print(gaps)