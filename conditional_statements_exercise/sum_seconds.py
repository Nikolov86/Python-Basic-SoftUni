from math import floor

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
#колко минути е сборът от секунди целочислено деление
seconds = total_time % 60
#изчислете секундите с помощта на деление с остатък
minutes = floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")

else:
    print(f"{minutes}:{seconds}")