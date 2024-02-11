decorations_quantity = int(input())
days_left_until_xmas = int(input())
ornament_set = 2
tree_skirt = 5
garland = 3
lights = 15
total_costs = 0
xmas_spirit = 0

for curr_day in range(1, days_left_until_xmas + 1):
    if curr_day % 11 == 0:
        decorations_quantity += 2
    if curr_day % 2 == 0:
        total_costs += decorations_quantity * ornament_set
        xmas_spirit += 5
    if curr_day % 3 == 0:
        total_costs += decorations_quantity * (tree_skirt + garland)
        xmas_spirit += 3 + 10
    if curr_day % 5 == 0:
        total_costs += decorations_quantity * lights
        xmas_spirit += 17
        if curr_day % 3 == 0:
            xmas_spirit += 30
    if curr_day % 10 == 0:
        xmas_spirit -= 20
        total_costs += tree_skirt + garland + lights
if days_left_until_xmas % 10 == 0:
    xmas_spirit -= 30

print(f'Total cost: {total_costs}')
print(f'Total spirit: {xmas_spirit}')

