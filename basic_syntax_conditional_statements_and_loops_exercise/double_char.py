command = input()

while command != 'End':
    if command != 'SoftUni':
        for char in command:
            char *= 2
            print(char, end='')
        print()
    command = input()

