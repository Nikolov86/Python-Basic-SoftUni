sea_packages = int(input())
mountain_packages = int(input())

sea_price = 680
mountain_price = 499

total_profit = 0
all_sold = False

while True:
    command = input()
    if command == "Stop":
        break
    elif command == "sea":
        if sea_packages > 0:
            total_profit += sea_price
            sea_packages -= 1
            if sea_packages == 0 and mountain_packages == 0:
                all_sold = True
        else:
            continue
    elif command == "mountain":
        if mountain_packages > 0:
            total_profit += mountain_price
            mountain_packages -= 1
            if sea_packages == 0 and mountain_packages == 0:
                all_sold = True
                break

if all_sold:
    print("Good job! Everything is sold.")
    print(f"Profit: {total_profit} leva.")
else:
    print(f"Profit: {total_profit} leva.")
