import sys
import math
from functools import partial


def main():
    while 1:
        n = int(sys.stdin.readline().strip())
        if not n: break
        cards = [False] * n
        c = 0
        for i in range(n):
            card, word = sys.stdin.readline().strip().split()
            word_len = len(word)
            while word_len - 1:
                if not cards[c]:
                    word_len -= 1
                c = (c+1) % n
            while cards[c]:
                c = (c+1) % n
            cards[c] = card
        print(" ".join(cards))

if __name__ == "__main__":
    main()
