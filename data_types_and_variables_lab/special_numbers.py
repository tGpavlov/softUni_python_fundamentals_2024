# num = int(input())
#
# for current_num in range(1, num + 1):
#     digit_sum = 0
#     for digit in str(current_num):
#         digit_sum += int(digit)
#     if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
#         print(f'{current_num} -> True')
#     else:
#         print(f'{current_num} -> False')

# ===== solution with bool variable =====

num = int(input())

for current_num in range(1, num + 1):
    digit_sum = 0
    is_special = False
    for digit in str(current_num):
        digit_sum += int(digit)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True
    print(f'{current_num} -> {is_special}')
