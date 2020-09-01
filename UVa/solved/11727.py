import sys
import math


def main():
    t = int(sys.stdin.readline())
    for t in range(t):
        pays = list(map(int, sys.stdin.readline().strip().split()))
        if pays[0] > pays[1] > pays[2] or pays[0] < pays[1] < pays[2]: print(f"Case {t+1}: {pays[1]}")
        elif pays[0] > pays[2] > pays[1] or pays[0] < pays[2] < pays[1]: print(f"Case {t+1}: {pays[2]}")
        else: print(f"Case {t+1}: {pays[0]}")


if __name__ == "__main__":
    main()
