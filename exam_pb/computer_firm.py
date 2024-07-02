n = int(input())

total_sales = 0
total_rating = 0

for _ in range(n):
    sales_and_rating = input()
    sales = int(sales_and_rating[:-1])
    rating = int(sales_and_rating[-1])

    if rating == 2:
        sales *= 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85

    total_sales += sales
    total_rating += rating

average_rating = total_rating / n

print("{:.2f}".format(total_sales))
print("{:.2f}".format(average_rating))
