price_of_trip = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

price_of_toys = count_puzzles * 2.60 + \
                count_dolls * 3 + \
                count_bears * 4.10 + \
                count_minions * 8.20 + \
                count_trucks * 2

count_of_all_toys = count_puzzles + count_dolls + \
                    count_bears + count_minions + \
                    count_trucks

if count_of_all_toys >= 50:
     price_of_toys = price_of_toys * 0.75
else:
    price_of_toys * 0.75

rent = price_of_toys * 0.10

profit = price_of_toys - rent

if profit > price_of_trip:
  print(f"Yes! {profit - price_of_trip:.2f} lv left.")
else:
    print(f"Not enough money! {abs(profit - price_of_trip):.2f} lv needed.")