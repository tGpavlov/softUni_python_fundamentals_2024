# def chars_range(first_char, second_char):
#     result = ''
#
#     for char_index in range(ord(first_char) + 1, ord(second_char)):
#         result += chr(char_index) + ' '
#
#     return result
#
#
# first_character, second_character = input(), input()
# print(chars_range(first_character, second_character))

chars_range = lambda first_char, second_char: ' '.join(map(chr, range(ord(first_char) + 1, ord(second_char))))
first_character, second_character = input(), input()
print(chars_range(first_character, second_character))
