# list_of_names = input().split(', ')
# sorted_list = sorted(list_of_names, key=lambda x: (-len(x), x))
# print(sorted_list)
#

def sort_names():
    list_of_names = input().split(', ')

    sorted_list = sorted(list_of_names, key=lambda x: (-len(x), x))  # length and alphabet

    return sorted_list


result = sort_names()
print(result)