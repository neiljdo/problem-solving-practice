import sys
import math
import bisect


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n_sellers, n_buyers = list(map(int, sys.stdin.readline().strip().split()))
        sell_prices = sorted(list(map(int, sys.stdin.readline().strip().split())))
        buy_prices = sorted(list(map(int, sys.stdin.readline().strip().split())))
        all_prices_distinct = sorted(list(set([0] + sell_prices + buy_prices)))

        angry_count = n_sellers + n_buyers
        best_bid = math.inf

        # O(n log n) sort time complexity dominates O(n) linear search below
        # n is of order 10^4
        for i, bid in enumerate(all_prices_distinct):
            n_angry_sellers = n_sellers - bisect.bisect_right(sell_prices, bid)
            n_angry_buyers = bisect.bisect_left(buy_prices, bid)
            total_angry_at_bid = n_angry_buyers + n_angry_sellers
            
            if angry_count > total_angry_at_bid:
                angry_count = total_angry_at_bid
                best_bid = bid
            elif angry_count == total_angry_at_bid:
                angry_count = total_angry_at_bid
                best_bid = min(best_bid, bid)

        print(best_bid, angry_count)


if __name__ == "__main__":
    main()
