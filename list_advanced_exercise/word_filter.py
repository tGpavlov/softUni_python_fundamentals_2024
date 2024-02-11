text = input().split()
even_length_words = [word for word in text if len(word) % 2 == 0]
print('\n'.join(words for words in even_length_words))
