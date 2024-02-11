num_of_words = int(input())
pure_string = True

for curr_word in range(num_of_words):
    word = input()
    pure_string = True
    for char in word:
        word_ascii_num = ord(char)
        if word_ascii_num == 95 or word_ascii_num == 46 or word_ascii_num == 44:
            pure_string = False
            break
    if pure_string:
        print(f'{word} is pure.')
    else:
        print(f'{word} is not pure!')





