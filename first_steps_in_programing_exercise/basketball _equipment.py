treining_price_for_year = int(input())

price_of_basketball_shoes = treining_price_for_year - treining_price_for_year * 0.4
price_of_basketball_team = price_of_basketball_shoes - price_of_basketball_shoes * 0.2
price_of_basketball_per_ball = price_of_basketball_team / 4
price_of_basketball_accessories = price_of_basketball_per_ball / 5

TOTAL_PRICE = treining_price_for_year + price_of_basketball_shoes + price_of_basketball_team + \
              price_of_basketball_per_ball + price_of_basketball_accessories


print(TOTAL_PRICE)
