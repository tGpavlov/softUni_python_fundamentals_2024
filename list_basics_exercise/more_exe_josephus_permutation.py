people = [int(person) for person in input().split(' ')]
executed_person = int(input())
executed_person_index = executed_person - 1
start_index = 0
order_of_execution = []
for person in range(len(people)):
    start = (start_index + executed_person_index) % len(people)
    start_index = start
    order_of_execution.append(people.pop(start))

# order_of_execution_string = f'[{','.join(str(x) for x in order_of_execution)}]'
# print(order_of_execution_string)

order_of_execution_string = str(order_of_execution).replace(', ', ',')
print(order_of_execution_string)