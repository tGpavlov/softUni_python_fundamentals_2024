def calculations(a, b, operator):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        if b != 0:
            result = int(a / b)
        else:
            print('Division by Zero')
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


operator = input()
num1 = int(input())
num2 = int(input())
print(calculations(num1, num2, operator))
