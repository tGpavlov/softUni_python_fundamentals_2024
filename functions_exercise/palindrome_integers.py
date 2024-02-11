def palindrome_check(nums):
    result = ''

    for index in nums:
        if index[::] == index[::-1]:
            result += 'True\n'
        else:
            result += 'False\n'

    return result


numbers = input().split(', ')
print(palindrome_check(numbers))
