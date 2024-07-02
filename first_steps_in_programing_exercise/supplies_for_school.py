pack_pens = int(input())
pack_marker = int(input())
prep_cleaning = int(input())
discount = int(input())

price_of_pack_pens = pack_pens * 5.80
price_of_pack_marker = pack_marker * 7.20
litters_prep_for_cleaning = prep_cleaning * 1.20
discount_all = discount / 100

price_of_all_matherials = price_of_pack_pens + price_of_pack_marker + litters_prep_for_cleaning
discount_price = price_of_all_matherials -(price_of_all_matherials * discount_all)

print(discount_price)