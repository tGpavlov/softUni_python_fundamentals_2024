def order_total_price(quantity, product):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'water':
        return quantity
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'snacks':
        return quantity * 2


name_of_product = input()
quantity_of_product = int(input())
result = order_total_price(quantity_of_product, name_of_product)
print(f'{result:.2f}')