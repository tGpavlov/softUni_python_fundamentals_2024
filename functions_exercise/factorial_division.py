def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def factorial_division(num1, num2):
    first_factorial = factorial(num1)
    second_factorial = factorial(num2)
    result = first_factorial / second_factorial

    return f'{result:.2f}'


first_number, second_number = int(input()), int(input())
print(factorial_division(first_number, second_number))
