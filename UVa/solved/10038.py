import sys
import math


def main():
    for line in sys.stdin:
        case = list(map(int, line.strip().split()))
        n = case[0]
        nums = case[1:]

        found = [False] * (n - 1)
        jolly = False
        for i in range(n-1):
            diff = int(abs(nums[i] - nums[i+1]))
            if diff not in range(1, n): break
            found[diff - 1] = True

        jolly = all(found)
        if jolly: print("Jolly")
        else: print("Not jolly")


if __name__ == "__main__":
    main()
