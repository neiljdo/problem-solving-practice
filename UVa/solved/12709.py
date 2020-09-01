import sys
import math
import bisect

    
def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0: break

        # max h gives the largest downward acceleration
        max_h = -math.inf
        max_volume = -math.inf
        for ant in range(n):
            l, w, h = list(map(int, sys.stdin.readline().strip().split()))
            if h > max_h:
                max_h, max_volume = h, l * w * h
            elif h == max_h:
                volume = l * w * h
                if volume > max_volume:
                    max_volume = volume
        print(max_volume)


if __name__ == "__main__":
    main()
