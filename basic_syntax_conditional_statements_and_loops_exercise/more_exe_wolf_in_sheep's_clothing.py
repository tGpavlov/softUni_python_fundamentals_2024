# import re
animals = input()
animals_list = animals.split(', ')
# animals_list = re.split(', ', animals)
animals_list.reverse()

for i in range(len(animals_list)):
    if animals_list[0] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    elif animals_list[i] == 'wolf':
        print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')
