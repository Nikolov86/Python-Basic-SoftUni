num = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, num + 1):
    curr_number = int(input())
    if i % 2 == 0:
        even_sum += curr_number
    else:
        odd_sum += curr_number

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {diff}')
