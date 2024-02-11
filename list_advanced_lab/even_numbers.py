# list_of_numbers = list(map(int, input().split(', ')))
#
# list_of_even_index = []
#
# for index, number in enumerate(list_of_numbers):                                 # 1st solution
#     if number % 2 == 0:
#         list_of_even_index.append(index)
#
# print(list_of_even_index)
# ----------------------------------------------------------------
# list_of_numbers = list(map(int, input().split(', ')))                            # 2nd solution
#
# even_indices = [index for index, number in enumerate(list_of_numbers) if number % 2 == 0]
#
# print(even_indices)
# ----------------------------------------------------------------
#                                                                                  # 3rd solution
list_of_numbers = list(map(int, input().split(', ')))
found_indices_or_no = map(lambda x: x if list_of_numbers[x] % 2 == 0 else 'no', range(len(list_of_numbers)))
even_indices = list(filter(lambda a: a != 'no', found_indices_or_no))
print(list(even_indices))
