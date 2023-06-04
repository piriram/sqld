T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = prices[-1]
    profit = 0

    for i in range(N-2, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]
    
    print(profit)
