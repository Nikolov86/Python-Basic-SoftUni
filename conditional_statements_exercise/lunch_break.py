from math import ceil,floor

serial_name = input()
episode = int(input())
rest_time = int(input())

launch_time = rest_time / 8
time_rest = rest_time / 4

left_time = rest_time - launch_time - time_rest


if left_time >= episode:
    left_time_ceil = ceil(left_time)
    free_time = left_time - episode
    print(f"You have enough time to watch {serial_name} and left with {free_time} minutes free time.")
else:
    free_time = floor( left_time - episode)
    print(f"You don't have enough time to watch {serial_name}, you need {abs(free_time)} more minutes.")
