price_veg = float(input())
price_fruit = float(input())
total_veg = int(input())
total_fruit = int(input())
euro = 1.94

veg = price_veg * total_veg
fruit = price_fruit * total_fruit

total = veg + fruit

transfer = total / euro

print(f"{transfer:.2f}")
