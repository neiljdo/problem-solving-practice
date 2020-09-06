import sys
import math
import re


def main():
    vocab = set()
    for line in sys.stdin:
        line = re.sub(r"[^a-zA-Z]+", " ", line)
        tokens = line.strip().split()
        for token in tokens:
            token = token.lower()
            vocab.add(token)
    
    vocab = sorted(list(vocab))
    for word in vocab:
        print(word)



if __name__ == "__main__":
    main()
