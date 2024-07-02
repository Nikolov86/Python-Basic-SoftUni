n = int(input())
numbers = []

# Четене на числата от потребителя и добавяне в списъка numbers
for i in range(n):
    num = int(input())
    numbers.append(num)

# Намиране на най-големия елемент в списъка
max_num = max(numbers)

# Изчисляване на сумата на всички числа без най-големия
sum_except_max = sum(numbers) - max_num

# Проверка дали съществува число, което е равно на сумата на всички останали
if max_num == sum_except_max:
    print("Yes")
    print("Sum =", max_num)
else:
    diff = abs(max_num - sum_except_max)
    print("No")
    print("Diff =", diff)
