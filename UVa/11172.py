import sys
import math


def main():
    n = int(sys.stdin.readline())
    for n in range(n):
        comp = list(map(int, sys.stdin.readline().split()))
        if comp[0] < comp[1]: print("<")
        elif comp[0] > comp[1]: print(">")
        else: print("=")

if __name__ == "__main__":
    main()
