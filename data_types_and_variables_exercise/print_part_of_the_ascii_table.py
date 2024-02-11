# original code
# =======================================
# start_char_index = int(input())
# end_char_index = int(input())
#
# for index in range(start_char_index, end_char_index + 1):
#     print(chr(index), end=' ')

# how to remove the whitespace in the end
# =======================================
start_char_index = int(input())
end_char_index = int(input())
final_string = ''
for index in range(start_char_index, end_char_index + 1):
    final_string += f'{chr(index)} '
print(final_string.rstrip())    # remove the whitespace on the right side of the string

# print(final_string[:-1])       # other option with slicing

