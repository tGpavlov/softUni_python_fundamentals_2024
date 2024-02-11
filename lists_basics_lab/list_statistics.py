number = int(input())
negative_integers = []
positive_integers = []

for current_integer in range(number):
    integer = int(input())
    if integer < 0:
        negative_integers.append(integer)
    else:
        positive_integers.append(integer)

print(positive_integers)
print(negative_integers)
print(f'Count of positives: {len(positive_integers)}')
print(f'Sum of negatives: {sum(negative_integers)}')
