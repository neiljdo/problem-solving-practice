import sys
import math


def main():
    n = int(sys.stdin.readline())
    digits = ["0"] * n
    # check 1st line for 1s
    line = sys.stdin.readline().strip()
    for i in range(n):
        if line[i*4:(i+1)*4] == ".*..": digits[i] = "1"
    for i in range(3):
        line = sys.stdin.readline().strip()

    for i in range(n):
        if digits[i] != "1":

            if line[i*4:(i+1)*4] == "*...": digits[i] = "2"
            else: digits[i] = "3"
    line = sys.stdin.readline()
    print("".join(digits))

if __name__ == "__main__":
    main()
