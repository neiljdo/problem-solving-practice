import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n0, n1, n2 = list(map(int, sys.stdin.readline().strip().split()))
    
    s = ""
    if n1:
        endsAtOne = False
        s = "01"
        if n1 % 2 == 0:
            if n2:
                s = "10"
                endsAtOne = True

        for _ in range(n1-1):
            if _ % 2 == 0:
                if not endsAtOne:
                    s += "0"
                else:
                    s += "1"
            else:
                if not endsAtOne:
                    s += "1"
                else:
                    s += "0"

    zeroes, ones = "", ""
    if n0:
        zeroes = "0" * (n0 + 1)
    if n2:
        ones = "1" * (n2 + 1)

    if s and s[0] == "0":
        s = zeroes[:-1] + s
        if s:
            s += ones[1:]
        else:
            s = ones
    else:
        s = ones[:-1] + s
        if s:
            s += zeroes[1:]
        else:
            s = zeroes
    print(s)




    
    
