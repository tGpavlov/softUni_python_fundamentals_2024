word = input()
uppercase_list = []

for i in range(len(word)):
    if word[i].isupper():
        uppercase_list.append(i)

print(uppercase_list)
