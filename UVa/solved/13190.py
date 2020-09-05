import sys
import math
import heapq



class MedicineSched:
    def __init__(self, name=None, rank=None, period=None, time=None):
        self.name = name
        self.rank = rank
        self.period = period
        self.time = time
        if self.time is None:
            self.time = self.period
    
    def __lt__(self, other):
        if self.time == other.time:
            return self.rank < other.rank
        return self.time < other.time

    def __str__(self):
        return f"{self.time} {self.name}"


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        meds = []
        n_meds, k = list(map(int, sys.stdin.readline().strip().split()))
        for rank in range(n_meds):
            name, period = sys.stdin.readline().strip().split()
            period = int(period)
            heapq.heappush(meds, MedicineSched(
                name=name,
                rank=rank,
                period=period
            ))

        for _ in range(k):
            latest = heapq.heappop(meds)
            heapq.heappush(
                meds,
                MedicineSched(
                    name=latest.name,
                    rank=latest.rank,
                    time=latest.time + latest.period,
                    period=latest.period
                )
            )
            print(latest)


if __name__ == "__main__":
    main()
