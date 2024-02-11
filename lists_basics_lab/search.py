number = int(input())
word = input()
list_of_strings = []
filtered_list_of_strings = []

for current_string in range(number):
    string = input()
    list_of_strings.append(string)
    if word in string:
        filtered_list_of_strings.append(string)

print(list_of_strings)
print(filtered_list_of_strings)

