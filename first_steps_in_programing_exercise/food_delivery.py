count_chikan_menu = int(input())
count_fish_menu = int(input())
count_veg_menu = int(input())

price_chikan_menu = count_chikan_menu * 10.35
price_fish_menu = count_fish_menu * 12.40
price_veg_menu = count_veg_menu * 8.15
delivery_price = 2.50
TOTAL_PRICE_MENU = price_chikan_menu + price_fish_menu + price_veg_menu
sweet_price = TOTAL_PRICE_MENU * 0.20

TOTAL_PRICE_ORDER = TOTAL_PRICE_MENU + sweet_price + delivery_price

print(TOTAL_PRICE_ORDER)