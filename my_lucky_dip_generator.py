import random
from colorama import Fore

print(Fore.GREEN + '--------- Welcome to LUCKY DIP Generator ----------')
print()
num_of_lines = int(input(Fore.RED + 'Please choose  the number of lines you want to play: '))
print()
my_numbers = []
life_ball = []
for current_line in range(num_of_lines):
    while True:
        my_random_number = random.randint(1, 47)
        my_random_life_ball = random.randint(1, 10)
        if len(life_ball) < 1:
            life_ball.append(my_random_life_ball)
        if my_random_life_ball in life_ball:
            continue
        if my_random_number in my_numbers:
            continue
        else:
            my_numbers.append(my_random_number)
        if len(my_numbers) == 5:
            break
    print(Fore.YELLOW + f'< Your lucky numbers are > {sorted(my_numbers)} >|',
          f'< Life ball is > {sorted(life_ball)}', sep='')
    my_numbers = []
    life_ball = []
print()
print(Fore.GREEN + '      Thank you and Good Luck!!!      ')
