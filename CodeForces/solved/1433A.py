import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    respond = int(sys.stdin.readline().strip())

    digit = respond % 10
    out = 0
    for d in range(1, digit):
        out += 10
    
    if respond < 10:
        out += 1
    elif respond < 100:
        out += 3
    elif respond < 1000:
        out += 6
    elif respond < 10000:
        out += 10

    print(out)