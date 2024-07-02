trip_money = float(input())
jessy_money = float(input())

days_counter = 0
spending_counter = 0

while jessy_money < trip_money and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1

    if command == 'save':
        jessy_money += money
        spending_counter = 0
    elif command == 'spend':
        jessy_money -= money
        spending_counter += 1

    if jessy_money <= 0:
        jessy_money = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)
elif jessy_money >= trip_money:
    print(f'You saved the money for {days_counter} days.')
