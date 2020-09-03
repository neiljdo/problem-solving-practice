import sys
import math
from collections import deque



def main():
    while 1:
        line = sys.stdin.readline().strip()
        if not len(line): break

        strq = deque()
        to_left_buffer = False
        buffer = ""
        for c in line:
            if c == "[":
                to_left_buffer = True
                if buffer:
                    strq.appendleft(buffer)
                    buffer = ""
            else:
                if c != "]":
                    if to_left_buffer:
                        buffer += c
                    else:
                        strq.append(c)
                else:
                    if buffer:
                        strq.appendleft(buffer)
                        buffer = ""
                    to_left_buffer = False
            # print(f"buffer: {buffer}, strq: {strq}")
        
        strq.appendleft(buffer)

        print("".join(strq))


if __name__ == "__main__":
    main()
