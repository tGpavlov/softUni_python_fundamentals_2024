group_size = int(input())
days = int(input())
coins = 0

for index in range(1, days + 1):
    if index % 10 == 0:
        group_size -= 2
    if index % 15 == 0:
        group_size += 5
    coins += 50 - group_size * 2
    if index % 3 == 0:
        coins -= group_size * 3
    if index % 5 == 0:
        coins += group_size * 20
        if index % 3 == 0:
            coins -= group_size * 2

coins_per_companion = coins // group_size
print(f'{group_size} companions received {coins_per_companion} coins each.')
