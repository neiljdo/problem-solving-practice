import sys
import math


def main():
    t = 0
    while True:
        seq = sys.stdin.readline().strip()
        if seq == "end": break
        t += 1

        top_of_stacks = []
        for c in seq:
            if not top_of_stacks:
                top_of_stacks.append(c)
            else:
                new_stack = True
                for i, top in enumerate(top_of_stacks):
                    if top >= c:
                        top_of_stacks[i] = c
                        new_stack = False
                        break
                if new_stack:
                    top_of_stacks.append(c)

        print(f"Case {t}: {len(top_of_stacks)}")


if __name__ == "__main__":
    main()
