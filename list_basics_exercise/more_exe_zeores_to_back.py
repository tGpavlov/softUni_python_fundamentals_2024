integer_list = (input()).split(', ')
null_count = 0
while '0' in integer_list:
    integer_list.remove('0')
    null_count += 1
for i in range(null_count):
    integer_list.append('0')
print([int(number) for number in integer_list])
