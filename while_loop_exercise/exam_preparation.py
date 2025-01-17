failed_threshold = int(input())
failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ''
has_failed = True

while failed_times < failed_threshold:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break

    grade = int(input())
    grades_sum += grade  # Добавяме оценката към общата сума на оценките
    solved_problems_count += 1  # Увеличаваме броя на решените задачи
    last_problem = problem_name

    if grade <= 4:
        failed_times += 1

if has_failed:
    print(f'You need a break, {failed_threshold} poor grades.')
else:
    print(f'Average score: {grades_sum / solved_problems_count:.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')
