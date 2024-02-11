number = int(input())

for char_one_index in range(number):
    for char_two_index in range(number):
        for char_three_index in range(number):
            char_one = chr(97 + char_one_index)
            char_two = chr(97 + char_two_index)
            char_three = chr(97 + char_three_index)
            print(f'{char_one}{char_two}{char_three}')
