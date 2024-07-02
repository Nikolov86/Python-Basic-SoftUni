ACC_BALANCE = 0

while True:
    word = input()

    if word == 'NoMoreMoney':
        break

    curr_sum = float(word)  # preformat str = number

    if curr_sum >= 0:
        ACC_BALANCE += curr_sum
        print(f'Increase: {curr_sum:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {ACC_BALANCE:.2f}')
