budget = int(input())
total_price = 0

while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break

    product_price = int(command)
    total_price += product_price

    if total_price > budget:
        print('You went in overdraft!')
        break
