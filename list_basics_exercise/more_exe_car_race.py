race_time = [int(number) for number in input().split()]
left_car_time = 0
right_car_time = 0

for left_car in range(len(race_time) // 2):
    if race_time[left_car] == 0:
        left_car_time *= 0.8
    else:
        left_car_time += race_time[left_car]
for right_car in range(len(race_time) - 1, len(race_time) // 2, -1):
    if race_time[right_car] == 0:
        right_car_time *= 0.8
    else:
        right_car_time += race_time[right_car]

if left_car_time > right_car_time:
    print(f'The winner is right with total time: {right_car_time:.1f}')
else:
    print(f'The winner is left with total time: {left_car_time:.1f}')