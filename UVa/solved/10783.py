import sys
import math


def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        a = int(sys.stdin.readline().strip())
        b = int(sys.stdin.readline().strip())
        if a % 2 == 0: a += 1
        if b % 2 == 0: b -= 1
        n = (b-a) // 2 + 1
        out = (a + b) * n // 2
        print(f"Case {i+1}: {out}")


if __name__ == "__main__":
    main()
