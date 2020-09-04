import sys
import math


def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        print(f"Case #{i+1}:")
        by1 = set(map(int, sys.stdin.readline().strip().split()[1:]))
        by2 = set(map(int, sys.stdin.readline().strip().split()[1:]))
        by3 = set(map(int, sys.stdin.readline().strip().split()[1:]))

        distinct = [[], [], []]
        for p in by1:
            if p not in by2 and p not in by3:
                distinct[0].append(p)
        for p in by2:
            if p not in by3 and p not in by1:
                distinct[1].append(p)
        for p in by3:
            if p not in by2 and p not in by1:
                distinct[2].append(p)
        # print(distinct)
        max_probs = max([len(probs) for probs in distinct])
        for i, probs in enumerate(distinct):
            if len(probs) == max_probs:
                print(f"{i+1} {max_probs} {' '.join([str(p) for p in sorted(probs)])}".strip())


if __name__ == "__main__":
    main()
