num = int(input())

list_of_integers = []
filtered_list_of_integers = []

for current_integer in range(num):
    integer = int(input())
    list_of_integers.append(integer)

command = input()
# --------------------------------comprehension solution---------------------------------------
if command == 'even':
    filtered_list_of_integers = [num for num in list_of_integers if num % 2 == 0]
elif command == 'odd':
    filtered_list_of_integers = [num for num in list_of_integers if num % 2 != 0]
elif command == 'negative':
    filtered_list_of_integers = [num for num in list_of_integers if num < 0]
else:
    filtered_list_of_integers = [num for num in list_of_integers if num >= 0]
# ---------------------------------------------------------------------------------------------

# if command == 'even':
#     for num in list_of_integers:
#         if num % 2 == 0:
#             filtered_list_of_integers.append(num)
# elif command == 'odd':
#     for num in list_of_integers:
#         if num % 2 != 0:
#             filtered_list_of_integers.append(num)
# elif command == 'positive':
#     for num in list_of_integers:
#         if num >= 0:
#             filtered_list_of_integers.append(num)
# else:
#     for num in list_of_integers:
#         if num < 0:
#             filtered_list_of_integers.append(num)


print(filtered_list_of_integers)
