budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price_per_loaf = (flour_price * 1.25) / 4
cost_per_loaf = flour_price + eggs_price + milk_price_per_loaf
loaf_count = 0
coloured_eggs = 0

while budget > cost_per_loaf:
    budget -= cost_per_loaf
    loaf_count += 1
    coloured_eggs += 3
    if loaf_count % 3 == 0:
        coloured_eggs -= loaf_count - 2

print(f'You made {loaf_count} loaves of Easter bread!'
      f' Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')