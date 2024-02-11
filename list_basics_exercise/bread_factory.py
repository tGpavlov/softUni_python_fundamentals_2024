events = input().split('|')
initial_energy = 100
initial_coins = 100
is_closed = False

for event in events:
    event, value = event.split('-')
    value = int(value)
    if event == 'rest':
        current_energy = initial_energy
        initial_energy += value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f'You gained {gained_energy} energy.', f'Current energy: {initial_energy}.', sep='\n')
    elif event == 'order':
        if initial_energy >= 30:
            initial_coins += value
            initial_energy -= 30
            print(f'You earned {value} coins.')
        else:
            initial_energy += 50
            print('You had to rest!')
            
    else:
        if initial_coins >= value:
            initial_coins -= value
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            is_closed = True
            break

if not is_closed:
    print('Day completed!', f'Coins: {initial_coins}', f'Energy: {initial_energy}', sep='\n')

