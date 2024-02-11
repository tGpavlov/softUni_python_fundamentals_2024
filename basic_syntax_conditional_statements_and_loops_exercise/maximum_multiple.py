# divisor = int(input())
# boundary = int(input())
#
# for num in range(boundary, divisor - 1, -1):
#     if num % divisor == 0:
#         print(num)
#         break

# alternate solution

divisor = int(input())
boundary = int(input())

number = (boundary // divisor) * divisor

print(number)