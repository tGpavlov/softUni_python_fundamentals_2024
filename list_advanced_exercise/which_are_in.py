# first_sequence = input().split(', ')
# second_sequence = input().split(', ')
#
# new_string_list = []
#
# for first_string in first_sequence:
#     for second_string in second_sequence:
#         if first_string in second_string:
#             new_string_list.append(first_string)
#             break
#
# print(new_string_list)

first_sequence = input().split(', ')
second_sequence = input().split(', ')
print([first_str for first_str in first_sequence if any(first_str in second_str for second_str in second_sequence)])