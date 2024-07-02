safety_nylon = int(input())
paint = int(input())
thinner_for_painting = int(input())
hours = int(input())


safety_nylon_sum = (safety_nylon + 2) * 1.50
paint_sum = (paint + paint * 0.10) * 14.50
thinner_for_painting_sum = thinner_for_painting * 5.00
bags_sum = 0.40
total_sum_math = safety_nylon_sum + paint_sum + thinner_for_painting_sum + bags_sum
worker_sum = (total_sum_math * 0.30) * hours
TOTAL_SUM = total_sum_math + worker_sum

print(TOTAL_SUM)
