rest = int(float(input()) * 100)
coins = [200, 100, 50, 20, 10, 5, 2, 1]
coin_count = 0

for coin in coins:
    count = rest // coin
    coin_count += count
    rest -= count * coin

print(coin_count)


"""Използване на цялочислено деление
number = 3.14159
integer_part = int(number)
print(integer_part)
"""