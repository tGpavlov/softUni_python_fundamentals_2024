# def even_num_list(nums):
#     even_list = []
#
#     for digit in nums:
#
#         if int(digit) % 2 == 0:
#             even_list.append(int(digit))
#
#     return even_list
#
#
# numbers_str = input().split()
# print(even_num_list(numbers_str))


# def is_even(num):
#
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# numbers = list(map(int, input().split()))
# even_nums = list(filter(is_even, numbers))
# print(even_nums)


numbers = list(map(int, input().split()))
even_nums = list(filter(lambda num: num % 2 == 0, numbers))
print(even_nums)