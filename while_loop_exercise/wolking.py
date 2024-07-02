goal_step = 10_000
total_step = 0

while total_step < goal_step:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        total_step += steps_to_home
        if total_step < goal_step:
            diff = goal_step - total_step
            print(f'{diff} more steps to reach goal.')
        break
    else:
        steps = int(command)
        total_step += steps

if total_step >= goal_step:
    diff = goal_step - total_step
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")