def happy_employee_check():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())

    improved_happiness = [num * happiness_factor for num in happiness_list]
    average_happiness = sum(improved_happiness) / len(happiness_list)

    happy_employees = sum(num >= average_happiness for num in improved_happiness)
    total_happiness = len(improved_happiness)

    message = 'happy' if happy_employees >= total_happiness / 2 else 'not happy'
    result = f'Score: {happy_employees}/{total_happiness}. Employees are {message}!'

    return result


print(happy_employee_check())
