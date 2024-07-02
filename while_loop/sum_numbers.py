BASE_NUMBER = int(input())
current_num = 0

while True:
    current_sum = int(input())
    current_num += current_sum

    if current_num >= BASE_NUMBER:
        print(current_num)
        break

