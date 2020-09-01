import sys
import math
from functools import partial


def main():
    start = True
    for line in sys.stdin:
        while True:
            if '"' not in line: break
            else:
                loc = line.index('"')
                line = line[:loc] + ("``" if start else "''") + line[loc+1:]
                start = not start
        print(line.strip())

if __name__ == "__main__":
    main()
