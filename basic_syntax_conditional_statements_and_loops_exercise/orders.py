num_of_orders = int(input())
total_amount = 0

for curr_order in range(num_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 \
            and 1 <= capsule_needed_per_day <= 2000:

        order_amount = (price_per_capsule * capsule_needed_per_day) * days
        total_amount += order_amount

        print(f'The price for the coffee is: ${order_amount:.2f}')
    else:
        continue

print(f'Total: ${total_amount:.2f}')
