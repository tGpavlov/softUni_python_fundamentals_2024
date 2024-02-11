# number_of_lines = int(input())
# opening_brackets = 0
# closing_brackets = 0
# is_balanced = True
#
# for current_line in range(number_of_lines):
#     symbol_in_line = input()
#     if symbol_in_line == ')' and closing_brackets == 0 and opening_brackets == 0:
#         is_balanced = False
#         break
#     if symbol_in_line == '(':
#         opening_brackets += 1
#     if symbol_in_line == ')':
#         closing_brackets += 1
#     if abs(opening_brackets - closing_brackets) >= 2:
#         is_balanced = False
#         break
#
# if opening_brackets == closing_brackets and is_balanced:
#     print('BALANCED')
# else:
#     print('UNBALANCED')

# ===========================================================================
# ===========================================================================


lines = int(input())

is_balanced = True
last_bracket = ''
for _ in range(0, lines):
    current = input()
    if current not in ['(', ')']:
        continue

    if last_bracket == '' and current == ')' or last_bracket == current:
        is_balanced = False
        break

    last_bracket = current

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')