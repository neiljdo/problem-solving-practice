import sys
import math
import heapq



class Tick:
    def __init__(self, q_num=None, period=None, time=None):
        self.q_num = q_num
        self.period = period
        self.time = time
        if self.time is None:
            self.time = self.period
    
    def __lt__(self, other):
        if self.time == other.time:
            return self.q_num < other.q_num
        return self.time < other.time


def main():
    ticks = []
    while True:
        line = sys.stdin.readline().strip()
        if line == "#": break
        q_num, period = list(map(int, line.split()[1:]))
        heapq.heappush(ticks, Tick(q_num=q_num, period=period))

    k = int(sys.stdin.readline().strip())
    for _ in range(k):
        latest = heapq.heappop(ticks)
        heapq.heappush(
            ticks,
            Tick(
                q_num=latest.q_num,
                time=latest.time + latest.period,
                period=latest.period
            )
        )
        print(latest.q_num)


if __name__ == "__main__":
    main()
