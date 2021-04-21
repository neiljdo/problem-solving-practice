import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    candies = list(map(int, sys.stdin.readline().strip().split()))
    
    nMoves = 0
    remaining = len(candies)
    sumA, sumB, prevTurnSum = 0, 0, 0
    a, b = 0, len(candies) - 1
    aliceTurn = True
    while a <= b:
        turnSum = 0
        while turnSum <= prevTurnSum and remaining:
            if aliceTurn:
                turnSum += candies[a]
                a += 1
                remaining -= 1
            else:
                turnSum += candies[b]
                b -= 1
                remaining -= 1
        # print(candies[a:b+1], prevTurnSum, turnSum)
        sumA += turnSum * aliceTurn
        sumB += turnSum * (not aliceTurn)
        nMoves += 1
        aliceTurn = not aliceTurn
        prevTurnSum = turnSum
    print(nMoves, sumA, sumB)
