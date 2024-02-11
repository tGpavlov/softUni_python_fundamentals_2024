from math import ceil

num_of_persons = int(input())
capacity = int(input())

courses = ceil(num_of_persons / capacity)

print(courses)