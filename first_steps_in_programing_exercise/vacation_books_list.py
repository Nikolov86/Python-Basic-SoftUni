import math

number_of_pages = int(input())
pages = int(input())
the_number_of_days = int(input())

total_time_to_read_the_book = number_of_pages / pages
hours_of_day_for_reading = math.floor(total_time_to_read_the_book / the_number_of_days)

print(hours_of_day_for_reading)