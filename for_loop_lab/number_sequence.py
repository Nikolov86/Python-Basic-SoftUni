def find_min_max(numbers):
    if not numbers:
        return None, None  # Връщаме None за най-малкото и най-голямото число, ако няма въведени числа

    min_num = min(numbers)
    max_num = max(numbers)
    return min_num, max_num


n = int(input())
input_numbers = []

for _ in range(n):
    num = int(input())
    input_numbers.append(num)

min_num, max_num = find_min_max(input_numbers)

if min_num is not None and max_num is not None:
    print("Max number:", max_num)
    print("Min number:", min_num)
else:
    print("Не са въведени числа.")
