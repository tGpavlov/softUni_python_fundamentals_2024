gifts = input().split()
command = input().split()

while ('No' and 'Money') not in command:
    if 'OutOfStock' in command:
        if command[1] in gifts:
            while command[1] in gifts:
                target_index = gifts.index(command[1])
                gifts[target_index] = 'None'
    if 'Required' in command:
        if 0 < int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]
    if 'JustInCase' in command:
        gifts[-1] = command[1]

    command = input().split()

while 'None' in gifts:
    gifts.remove('None')
print(' '.join(gifts))
