# numbers = input().split()
# round_value = [round(float(number)) for number in numbers]
# print(round_value)

numbers = input().split()
round_value = []
for number in numbers:
    round_value.append(round(float(number)))
print(round_value)