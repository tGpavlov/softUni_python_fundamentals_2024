list_of_numbers = [int(number) for number in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))

list_of_numbers = [str(number) for number in list_of_numbers]
print(', '.join(list_of_numbers))

