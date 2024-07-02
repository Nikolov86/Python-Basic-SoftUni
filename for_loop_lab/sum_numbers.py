def sum_of_numbers(n):
    total_sum = 0
    for _ in range(n):
        num = int(input())
        total_sum += num
    return total_sum

n = int(input())
result = sum_of_numbers(n)
print(result)
