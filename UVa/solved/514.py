import sys
import math
from functools import partial

def is_possible(b_seq, n):
    stack = []
    to_push = 1
    while b_seq:
        if to_push == b_seq[0]:
            b_seq = b_seq[1:]
        elif stack and b_seq[0] == stack[-1]:
            b_seq = b_seq[1:]
            stack.pop()
            continue
        else:
            # push to stack iff <= n
            if to_push < n:
                stack.append(to_push)
            elif stack and stack[-1] != n:
                stack.append(to_push)
            else:
                break
        to_push = min(to_push + 1, n)
        # print(b_seq, stack, to_push)
    
    return not b_seq and not stack


def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if n:
            while True:
                b_seq = sys.stdin.readline().strip()
                if b_seq == "0":
                    print()
                    break
                
                b_seq = list(map(int, b_seq.split()))
                print("Yes" if is_possible(b_seq, n) else "No")
        else:
            break


if __name__ == "__main__":
    main()
