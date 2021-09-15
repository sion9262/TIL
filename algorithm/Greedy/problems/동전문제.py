coins = [1, 50, 100, 500]

def min_coin(pay, coins):
    total = 0
    details = []
    # 큰 순으로 정렬
    coins.sort(reverse=True)

    for coin in coins:
        count = pay // coin
        total += count
        pay -= coin * count
        details.append((coin, count))
    return total, details

print(min_coin(4720, coins))