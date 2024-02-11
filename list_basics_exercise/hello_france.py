collection_of_items = input().split('|')
budget = float(input())
profit = 0
increased_item_price_list = []

for items in collection_of_items:
    item_type, item_price = items.split('->')
    item_price = float(item_price)
    in_range = False
    if item_type == 'Clothes':
        if item_price <= 50.00:
            in_range = True
    if item_type == 'Shoes':
        if item_price <= 35.00:
            in_range = True
    if item_type == 'Accessories':
        if item_price <= 20.50:
            in_range = True
    if in_range:
        if budget >= item_price:
            budget -= item_price
            profit += item_price * 0.4
            markup_item = item_price * 1.4
            increased_item_price_list.append(markup_item)

for price in increased_item_price_list:
    print(f'{price:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if sum(increased_item_price_list) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
