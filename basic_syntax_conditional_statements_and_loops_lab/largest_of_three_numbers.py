num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 >= num_2 and num_1 >= num_3:
    print(num_1)
elif num_2 >= num_1 and num_2 >= num_3:
    print(num_2)
else:
    print(num_3)

# different solution
num_1, num_2, num_3 = int(input()), int(input()), int(input())
print(max(num_1, num_2, num_3))
