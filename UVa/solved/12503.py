import sys
import math


def main():
    t = int(sys.stdin.readline())
    for t in range(t):
        steps = []
        n = int(sys.stdin.readline())
        for i in range(n):
            step = sys.stdin.readline().strip()
            if step == "LEFT": steps.append(-1)
            elif step == "RIGHT": steps.append(1)
            else:
                ref = int(step.split()[-1])
                steps.append(steps[ref - 1])
        print(sum(steps))


if __name__ == "__main__":
    main()
