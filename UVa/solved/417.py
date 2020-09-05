import sys
import math
import bisect


def main():
    # Build word index
    prefix = list("abcdefghijklmnopqrstuvwxyz")

    cache = {}
    ix = 1
    for c in prefix:
        cache[c] = ix
        ix += 1

    for _ in range(2, 6):
        temp = []
        for p in prefix:
            for i in range(ord(p[-1]) + 1, ord('z') + 1):
                temp.append(p + chr(i))
                cache[temp[-1]] = ix
                ix += 1
        prefix = temp

    while True:
        q = sys.stdin.readline().strip()
        if not len(q): break
        print(cache.get(q, 0))


if __name__ == "__main__":
    main()
