fires_with_cells = input().split('#')
water = int(input())
total_fire = 0
effort = 0
fire_out_cells = []
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)

for cell in fires_with_cells:
    # fire_type, cell_value = cell.split(' = ')  # when is only 2 values in index
    # cell_value = int(cell_value)
    fire_type_cell_value = cell.split(' = ')
    fire_type = fire_type_cell_value[0]
    cell_value = int(fire_type_cell_value[1])
    is_fire_valid = False
    if fire_type == 'High':
        if cell_value in high:
            is_fire_valid = True
    elif fire_type == 'Medium':
        if cell_value in medium:
            is_fire_valid = True
    elif fire_type == 'Low':
        if cell_value in low:
            is_fire_valid = True
    if is_fire_valid:
        if water >= cell_value:
            water -= cell_value
            total_fire += cell_value
            effort += cell_value * 0.25
            fire_out_cells.append(cell_value)

print('Cells:')
for index in fire_out_cells:
    print(f' - {index}')
print(f'Effort: {effort:.2f}', f'Total Fire: {total_fire}', sep='\n')