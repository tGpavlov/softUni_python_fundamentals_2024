neighborhood_list = [int(x) for x in input().split('@')]
command = input().split()
current_index = 0

while command[0] != 'Love!':
    jump_index = int(command[1])
    current_index += jump_index

    if current_index < len(neighborhood_list):
        if neighborhood_list[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood_list[current_index] -= 2
            if neighborhood_list[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")

    else:
        current_index = 0
        if neighborhood_list[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood_list[current_index] -= 2
            if neighborhood_list[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")

    command = input().split()

print(f"Cupid's last position was {current_index}.")

if sum(neighborhood_list) == 0:
    print(f"Mission was successful.")
else:
    failed_places = [x for x in neighborhood_list if x != 0]
    print(f"Cupid has failed {len(failed_places)} places.")

# counter = 0
# for n in neighborhood_list:
#     if n > 0:
#         counter += 1
#
# print(f"Cupid's last position was {current_index}.")
# if not counter == 0:
#     print(f"Cupid has failed {counter} places.")
# else:
#     print("Mission was successful.")

# print(f"Cupid's last position was {current_index}.")

# if sum(neighborhood_list) == 0:
#     print("Mission was successful.")
# else:
#     failed_houses = [house for house in neighborhood_list if house != 0]
#     print(f"Cupid has failed {len(failed_houses)} places.")
