def calculate_vowel_sum(text):
    vowel_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    sum = 0
    for char in text:
        if char.lower() in vowel_values:
            sum += vowel_values[char.lower()]
    return sum


user_input = input()
result = calculate_vowel_sum(user_input)
print(result)
