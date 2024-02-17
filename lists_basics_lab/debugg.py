numbers = [int(num) for num in input().split()]

average = sum(numbers) / len(numbers)
greater_then_average = []
for num in numbers:
    if num > average:
        greater_then_average.append(num)
sorted_numbers = sorted(greater_then_average, reverse=True)
if not greater_then_average:
    print('No')
else:
    counter = 0
    for digit in sorted_numbers:
        if counter <= 5:
            print(digit, end=' ')
            counter += 1
