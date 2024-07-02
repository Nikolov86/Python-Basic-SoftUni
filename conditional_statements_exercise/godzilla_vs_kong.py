budget_for_movie = float(input())
count_of_actor = int(input())
price_of_cloth_for_one_actor = float(input())

decor = budget_for_movie * 0.10

amount_for_cloth = count_of_actor * price_of_cloth_for_one_actor

if count_of_actor > 150:
    amount_for_cloth *= 0.9

TOTAL_AMOUNT_FOR_MOVIE = amount_for_cloth + decor

difference = abs(budget_for_movie - TOTAL_AMOUNT_FOR_MOVIE)

if TOTAL_AMOUNT_FOR_MOVIE <= budget_for_movie:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")

else:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")