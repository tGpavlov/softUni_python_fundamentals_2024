command = input()
total_price = 0
taxes = 0

while True:
    if command == 'special' or command == 'regular':
        break
    part_price = float(command)
    if part_price < 0:
        print("Invalid price!")
        command = input()
        continue
    else:
        total_price += part_price
        taxes += part_price * 0.20
    command = input()
final_price = total_price + taxes

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    if command == 'special':
        discount = final_price * 0.9
        print(f'Total price: {discount:.2f}$')
    else:
        print(f'Total price: {final_price:.2f}$')
