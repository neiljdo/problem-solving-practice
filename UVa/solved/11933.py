import sys
import math


def main():
    for line in sys.stdin:
        n = line.strip()
        """
        110110101, t
        000000001

        011011010, f
        001101101, f
        000000001

        010010001
        100100100

        40
        00...00101000
        11...11011000
        00...00001000

        42
        101010
        100010
        011101
        001000
        """
        if n not in ["", "0"]:
            n_orig = int(n)
            n = n_orig
            bit_a = True
            a = 0
            j = 0
            while n:
                if (n & 1):
                    if bit_a:
                        a |= 1 << j
                        bit_a = False
                    else:
                        bit_a = True
                n >>= 1
                j += 1
            print(f"{a} {n_orig & (~a)}")
        else:
            break


if __name__ == "__main__":
    main()
