# num = int(input())
# capacity_of_water_tank = 255
# total_liters_of_water = 0
#
# for liter_of_water in range(num):
#     current_liters_of_water = int(input())
#     total_liters_of_water += current_liters_of_water
#     if total_liters_of_water > capacity_of_water_tank:
#         print('Insufficient capacity!')
#         total_liters_of_water -= current_liters_of_water
# print(total_liters_of_water)
#

# another_solution

num_of_lines = int(input())
tank_capacity = 255
for line in range(num_of_lines):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0:
        print('Insufficient capacity!')
        continue
    tank_capacity -= liters_of_water
print(255 - tank_capacity)