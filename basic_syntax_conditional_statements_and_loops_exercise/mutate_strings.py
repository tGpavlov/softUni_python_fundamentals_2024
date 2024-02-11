first_string = input()
second_string = input()
printed_string = first_string

for char_index in range(len(first_string)):
    left_side = second_string[:char_index + 1]
    right_side = first_string[char_index + 1:]
    new_string = left_side + right_side
    if new_string != printed_string:
        print(new_string)
    printed_string = new_string
