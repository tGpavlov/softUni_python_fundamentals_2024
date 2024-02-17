def swap(list_integers, index_one, index_two):
    list_integers[index_one], list_integers[index_two] \
        = list_integers[index_two], list_integers[index_one]

    return list_integers


def multiply(list_integers, index_one, index_two):
    result = list_integers[index_one] * list_integers[index_two]
    list_integers[index_one] = result

    # list_integers[index_one] *= list_integers[index_two]

    return list_integers


def array_modifier(integers):
    while True:
        command = input().split()
        action = command[0]

        if action == 'end':
            break

        if action == 'swap':
            index_1 = int(command[1])
            index_2 = int(command[2])
            swap(integers, index_1, index_2)
        elif action == 'multiply':
            index_1 = int(command[1])
            index_2 = int(command[2])
            multiply(integers, index_1, index_2)
        elif action == 'decrease':
            integers = [num - 1 for num in integers]

    return integers


list_of_integers = list(map(int, input().split()))

final_result = array_modifier(list_of_integers)
print(', '.join(str(char) for char in final_result))

# print(*array_modifier(list_of_integers), sep=', ')
