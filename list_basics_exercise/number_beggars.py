money_as_str = input().split(', ')
# money_as_integer = [int(money) for money in input().split(', ')]  # !!! comprehension !!!
number_of_beggars = int(input())

money_as_int = []
for money in money_as_str:
    money_as_int.append(int(money))

starting_index = 0
final_sum_take_home = []

for current_beggar in range(number_of_beggars):
    current_money_amount = 0
    for current_beggar_index in range(starting_index, len(money_as_str), number_of_beggars):
        current_money_amount += money_as_int[current_beggar_index]
    final_sum_take_home.append(current_money_amount)
    starting_index += 1

print(final_sum_take_home)

# money_as_integer = [int(money) for money in input().split(', ')]
# number_of_beggars = int(input())
# beggars = [0 for _ in range(number_of_beggars)]
#
# for index, num in enumerate(money_as_integer):
#     beggars[index % number_of_beggars] += num
#     i = index % number_of_beggars
#     print(i)
# print(beggars)
