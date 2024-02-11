# numbers = list(map(float, input().split()))
# abs_value_list = []
# for number in numbers:
#     abs_value_list.append(abs(number))
# print(abs_value_list)
#


numbers = input().split()
absolute_value = [abs(float(number)) for number in numbers]
print(absolute_value)