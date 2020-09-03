import sys
import math


def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        m, n = list(map(int, sys.stdin.readline().strip().split()))
        m_words, n_words = [], []
        for _ in range(m):
            m_words.append(sys.stdin.readline().strip())

        for _ in range(n):
            n_words.append(sys.stdin.readline().strip())

        concats = set()
        for m_word in m_words:
            for n_word in n_words:
                concats.add(m_word + n_word)
        
        print(f"Case {i+1}: {len(concats)}")
        
        
if __name__ == "__main__":
    main()
