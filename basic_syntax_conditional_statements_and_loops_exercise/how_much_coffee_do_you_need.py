command = input()

coffee_counter = 0
extra_sleep_needed = False

while command != 'END':
    if command == 'coding' or command == 'dog'\
            or command == 'cat' or command == 'movie':
        coffee_counter += 1
    elif command == 'CODING' or command == 'DOG'\
            or command == 'CAT' or command == 'MOVIE':
        coffee_counter += 2
    if coffee_counter > 5:
        extra_sleep_needed = True
    command = input()

if extra_sleep_needed:
    print('You need extra sleep')
else:
    print(coffee_counter)