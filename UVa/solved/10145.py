import sys
import math
from collections import defaultdict



class Lock:
    def __init__(self, mode=None, txn_id=None):
        self.mode = mode
        self.txn_id = txn_id

    def is_in_conflict(self, other):
        return all([
            self.txn_id != other.txn_id,
            self.mode == "X" or other.mode == "X"
        ])

    def __repr__(self):
        return f"{self.txn_id} {self.mode}"


def main():
    t = int(sys.stdin.readline().strip())

    for i in range(t):
        sys.stdin.readline().strip()
        manager = defaultdict(list)
        ignored_txns = set()
        while True:
            line = sys.stdin.readline().strip()

            if line != "#":
                mode, txn_id, item = line.split()
                if txn_id in ignored_txns:
                    print("IGNORED")
                else:
                    lock = Lock(mode=mode, txn_id=txn_id)
                    if item not in manager or not any([lock.is_in_conflict(prev) for prev in manager[item]]):
                        print("GRANTED")
                        manager[item].append(lock)
                    else:
                        print("DENIED")
                        ignored_txns.add(txn_id)
            else:
                break
        if i != t - 1: print("")
                

if __name__ == "__main__":
    main()
