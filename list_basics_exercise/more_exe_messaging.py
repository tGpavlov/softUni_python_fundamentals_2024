numbers = input().split()
text = input()
text_list = [index for index in text]
message = ''

for index_in_numbers in range(len(numbers)):
    index_sum = 0
    for index_sum_in_numbers in numbers[index_in_numbers]:
        index_sum += int(index_sum_in_numbers)
    if index_sum > len(text) - 1:
        index_sum -= len(text)
        message += text_list.pop(index_sum)
    else:
        message += text_list.pop(index_sum)

print(message)
