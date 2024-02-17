def increase_and_decrease_targets(targets, increase_and_decrease):
    for index in range(len(targets)):
        if targets[index] > increase_and_decrease and targets[index] != -1:
            targets[index] -= increase_and_decrease
        elif targets[index] <= increase_and_decrease and targets[index] != -1:
            targets[index] += increase_and_decrease
    return targets


def shot_targets(target_list):
    command = input()
    total_shot_targets = 0

    while command != 'End':
        target_position = int(command)

        if target_position < 0 or target_position >= len(target_list) or target_list[target_position] == -1:
            command = input()
            continue
        else:
            increase_and_decrease = target_list.pop(target_position)
            target_list.insert(target_position, -1)
            target_list = increase_and_decrease_targets(target_list, increase_and_decrease)
            total_shot_targets += 1
        command = input()
    targets_as_string = [str(x) for x in target_list]
    print(f"Shot targets: {total_shot_targets} -> {' '.join(targets_as_string)}")


targets = [int(number) for number in input().split()]
shot_targets(targets)
