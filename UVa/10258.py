import sys
import math
import bisect

    
def main():
    nums = []
    for line in sys.stdin:
        try:
            n = int(line.strip())
        except:
            break
        bisect.insort(nums, n)

        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            print((nums[mid - 1] + nums[mid]) // 2)
        else:
            print(nums[mid])


if __name__ == "__main__":
    main()
