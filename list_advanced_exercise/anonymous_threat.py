list_of_data = input().split()
first_command = input()

while first_command != '3:1':
    command = first_command.split()

    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(list_of_data) - 1:
            end_index = len(list_of_data) - 1
        merged_data = ''.join(list_of_data[start_index:end_index + 1])
        list_of_data = [word for word in list_of_data if word not in merged_data]
        list_of_data.insert(start_index, merged_data)

    elif command[0] == 'divide':
        index = int(command[1])
        partitions = int(command[2])

        if partitions > len(list_of_data[index]):
            step = 1
        else:
            step = len(list_of_data[index]) // partitions

        divided_data = list_of_data.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                list_of_data.insert(index, divided_data[start::])
                break
            else:
                list_of_data.insert(index, divided_data[start: start + step:])
            start += step
            index += 1

    first_command = input()

print(' '.join(list_of_data))
