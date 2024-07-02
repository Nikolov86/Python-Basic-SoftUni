# Входни данни
group_size = int(input())
nights = int(input())
transport_cards = int(input())
museum_tickets = int(input())

# Цените на услугите
night_price = 20
transport_price = 1.60
museum_price = 6

# Обща сума за всеки вид услуга
total_nights = group_size * nights
total_transport = group_size * transport_cards
total_museum = group_size * museum_tickets

# Обща сума преди начисляване на непредвидени разходи
total_cost = total_nights * night_price + total_transport * transport_price + total_museum * museum_price

# Начисляване на 25% за непредвидени разходи
unexpected_expenses = total_cost * 0.25

# Общата сума, която трябва да се плати от групата
total_payment = total_cost + unexpected_expenses

# Изход
print(f'{total_payment:.2f}')
