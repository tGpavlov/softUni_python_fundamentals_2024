def min_max_sum(nums):
    min_num = min(nums)
    max_num = max(nums)
    sum_of_nums = sum(nums)
    return min_num, max_num, sum_of_nums


numbers = list(map(int, input().split()))
min_number, max_number, sum_of_numbers = min_max_sum(numbers)

print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {sum_of_numbers}')
