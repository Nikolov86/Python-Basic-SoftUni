number = int(input())

first_digit = number % 10
second_digit = (number // 10) % 10
third_digit = number // 100

for i in range(1, first_digit + 1):
    for j in range(1, second_digit + 1):
        for k in range(1, third_digit + 1):
            result = i * j * k
            print(f"{i} * {j} * {k} = {result};")
