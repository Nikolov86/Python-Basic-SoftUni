t_shirt_price = float(input())
ball_price = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.20
sneakers_price = (t_shirt_price + shorts_price) * 2

total_price = t_shirt_price + shorts_price + socks_price + sneakers_price
discount = total_price * 0.15
total_price -= discount

if total_price >= ball_price:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_price:.2f} lv.')
else:
    needed_money = ball_price - total_price
    print("No, he will not earn the world-cup replica ball.")
    print(f'He needs {needed_money:.2f} lv. more.')
