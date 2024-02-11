# 1.0
word = input()

for i in range(len(word) - 1, -1, -1):
    print(word[i], end='')

# 1.1
word = input()

for char in word[::-1]:
    print(char, end='')

# example for 'range'

even_numbers = list(range(10, 20, 2))
print(even_numbers)


#
# def factorial(n):
#     if n == 1 or n == 0:
#         return 'kur'
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(0))
#
# a = 10 ** 0
# print(a)
