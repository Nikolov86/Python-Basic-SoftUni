n = int(input())
numbers = []

# Четене на числата от потребителя и добавяне в списъка numbers
for i in range(n):
    num = int(input())
    numbers.append(num)

# Инициализация на броячите за всяка категория
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

# Проучване на всяко число и увеличаване на съответния брояч
for num in numbers:
    if num < 200:
        count_p1 += 1
    elif num < 400:
        count_p2 += 1
    elif num < 600:
        count_p3 += 1
    elif num < 800:
        count_p4 += 1
    else:
        count_p5 += 1

# Пресмятане на процентите
total_numbers = len(numbers)
p1 = (count_p1 / total_numbers) * 100
p2 = (count_p2 / total_numbers) * 100
p3 = (count_p3 / total_numbers) * 100
p4 = (count_p4 / total_numbers) * 100
p5 = (count_p5 / total_numbers) * 100

# Отпечатване на резултата
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
