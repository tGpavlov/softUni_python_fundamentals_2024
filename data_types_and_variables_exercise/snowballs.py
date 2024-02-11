num_of_snowballs = int(input())
best_snowball = 0
best_weight = 0
best_time = 0
best_quantity = 0
for current_snowball in range(num_of_snowballs):
    weight = int(input())
    time = int(input())
    quantity = int(input())
    value_of_snowball = int((weight / time) ** quantity)
    if value_of_snowball > best_snowball:
        best_snowball = value_of_snowball
        best_weight = weight
        best_time = time
        best_quantity = quantity
print(f'{best_weight} : {best_time} = {best_snowball} ({best_quantity})')
