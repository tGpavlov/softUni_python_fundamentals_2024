def is_perfect_number(num):
    divisors_sum = sum(divisor for divisor in range(1, num) if num % divisor == 0)

    if divisors_sum == num:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'


number = int(input())
print(is_perfect_number(number))

# num = int(input())
# index_sum = 0
#
# for i in range(1, num):
#
#     if num % i == 0:
#         index_sum += i
#
# if num == index_sum:
#     print('oh yes')
