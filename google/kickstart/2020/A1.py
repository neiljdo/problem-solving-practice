def allocate(prices, budget):
    # print(f"allocating {budget} among {prices}")
    if budget <= 0 or len(prices) == 0:
        return 0

    return max(
        # we buy the first house
        (1 + allocate(prices[1:], budget - prices[0])) if prices[0] <= budget else -float("inf"),
        # we skip the first house
        allocate(prices[1:], budget)
    )
    

t = int(input().strip())
for i in range(t):
    n, budget = list(map(int, input().strip().split()))
    prices = list(map(int, input().strip().split()))

    optimal = allocate(prices, budget)

    print(f"Case #{i+1}: {optimal}")
