def positive_numbers(nums):
    return ', '.join([str(num) for num in nums if num >= 0])


def negative_numbers(nums):
    return ', '.join([str(num) for num in nums if num < 0])


def even_numbers(nums):
    return ', '.join([str(num) for num in nums if num % 2 == 0])


def odd_numbers(nums):
    return ', '.join([str(num) for num in nums if num % 2 != 0])


numbers = list(map(int, input().split(', ')))
print(f'Positive: {positive_numbers(numbers)}')
print(f'Negative: {negative_numbers(numbers)}')
print(f'Even: {even_numbers(numbers)}')
print(f'Odd: {odd_numbers(numbers)}')
