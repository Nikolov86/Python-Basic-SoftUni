num = input()
max_number = -1000000000

while num != 'Stop':
    number = int(num)

    if number > max_number:
        max_number = number

    num = input()

print(max_number)
