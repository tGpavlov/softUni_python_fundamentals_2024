def chair_availability(rooms):
    sum_total_chairs = 0

    for room in range(1, rooms + 1):
        number_of_chairs, visitors = input().split()
        total_chairs = len(number_of_chairs) - int(visitors)
        if int(visitors) > len(number_of_chairs):
            print(f'{abs(total_chairs)} more chairs needed in room {room}')
        sum_total_chairs += total_chairs

    return sum_total_chairs


number_of_rooms = int(input())
result = chair_availability(number_of_rooms)

if result >= 0:
    print(f'Game On, {result} free chairs left')