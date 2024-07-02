peter_budget = float(input())
video_card = int(input())
processor = int(input())
ram_memo = int(input())

price_video_card = video_card * 250
price_processor = (price_video_card * 0.35) * processor
price_ram_memo = (price_video_card * 0.10) * ram_memo

total_price = price_video_card + price_processor + price_ram_memo

discount = (total_price - total_price * 0.15)
money_left = abs(peter_budget - discount)

if video_card > processor and total_price <= peter_budget:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")