import sys
import math


def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        print(f"Case #{i+1}:")
        by1 = list(map(int, sys.stdin.readline().strip().split()))
        by2 = list(map(int, sys.stdin.readline().strip().split()))
        by3 = list(map(int, sys.stdin.readline().strip().split()))
        n1, by1 = by1[0], sorted(by1[1:])
        n2, by2 = by2[0], sorted(by2[1:])
        n3, by3 = by3[0], sorted(by3[1:])
        
        p1_dupe = []
        p2_dupe = []
        for p1 in by1:
            inb2 = p1 in by2
            if inb2:
                by2.remove(p1)
            inb3 = p1 in by3
            if inb3:
                by3.remove(p1)
            if inb2 or inb3: p1_dupe.append(p1)
        for p1 in p1_dupe:
            by1.remove(p1)

        for p2 in by2:
            if p2 in by3:
                by3.remove(p2)
                p2_dupe.append(p2)
        for p2 in p2_dupe:
            by2.remove(p2)

        max_distinct = max(len(by1), len(by2), len(by3))
        
        if len(by1) == max_distinct:
            by1s = " ".join([str(i) for i in sorted(by1)])
            print(f"1 {len(by1)} {by1s}")
        if len(by2) == max_distinct:
            by2s = " ".join([str(i) for i in sorted(by2)])
            print(f"2 {len(by2)} {by2s}")
        if len(by3) == max_distinct:
            by3s = " ".join([str(i) for i in sorted(by3)])
            print(f"3 {len(by3)} {by3s}")


if __name__ == "__main__":
    main()
