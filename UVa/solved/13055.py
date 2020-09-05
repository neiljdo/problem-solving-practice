import sys
import math


def main():
    nq = int(sys.stdin.readline().strip())
    dream_stack = []
    for _ in range(nq):
        q = sys.stdin.readline().strip().split()
        if q[0] == "Sleep":
            dream_stack.append(q[1])
        elif q[0] == "Kick":
            if len(dream_stack):
                dream_stack.pop()
        else:
            if len(dream_stack):
                print(dream_stack[-1])
            else:
                print("Not in a dream")
        # print(dream_stack)


if __name__ == "__main__":
    main()
