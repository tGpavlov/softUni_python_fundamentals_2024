sequence_of_numbers = [int(digit) for digit in input().split(', ')]
start_group = 10

while sequence_of_numbers:
    numbers_for_current_group = [num for num in sequence_of_numbers if num <= start_group]
    print(f'Group of {start_group}\'s: {numbers_for_current_group}')
    start_group += 10
    sequence_of_numbers = [num for num in sequence_of_numbers if num not in numbers_for_current_group]


