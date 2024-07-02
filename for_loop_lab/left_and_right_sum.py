def check_equal_sums(n, numbers):
    left_sum = sum(numbers[:n])
    right_sum = sum(numbers[n:])
    diff = abs(left_sum - right_sum)
    if left_sum == right_sum:
        print("Yes, sum =", left_sum)
    else:
        print("No, diff =", diff)

n = int(input())
input_numbers = []

for _ in range(2 * n):
    num = int(input())
    input_numbers.append(num)

check_equal_sums(n, input_numbers)

