import sys
import math


def main():
    for line in sys.stdin:
        m = int(line)
        if not m: break

        max_pow_2 = math.ceil(math.log(m, 2))
        max_pow_3 = math.ceil(math.log(m, 3))
        next_23 = math.inf
        for i in range(max_pow_2+1):
            for j in range(max_pow_3+1):
                candidate = (2 ** i) * (3 ** j)
                if candidate >= m:
                    next_23 = min(next_23, candidate)
        print(next_23)


if __name__ == "__main__":
    main()
