# import re
#
# word = input().lower()
# words_to_match = 'water', 'sun', 'fish', 'sand'
# pattern = '|'.join(words_to_match)
# matches = re.findall(pattern, word)
#
# print(len(matches))
# ====================================================
# text = input()
# text = text.lower()
#
# my_list = ["sand", "water", "fish", "sun"]
# counter = 0
#
# for item in my_list:
#     if item in text:
#         word_count_txt = text.count(item)
#         counter += word_count_txt
#
# print(counter)
# ====================================================
sentence = list(input().lower())
words = 0
for index in range(len(sentence)):
    if sentence[index] == "f" and index + 3 <= len(sentence):
        if sentence[index + 1] == "i" and sentence[index + 2] == "s" and sentence[index + 3] == "h":
            words += 1
    if sentence[index] == "s" and index + 3 <= len(sentence):
        if sentence[index + 1] == "a" and sentence[index + 2] == "n" and sentence[index + 3] == "d":
            words += 1
    if sentence[index] == "s" and index + 2 <= len(sentence):
        if sentence[index + 1] == "u" and sentence[index + 2] == "n":
            words += 1
    if sentence[index] == "w" and index + 4 <= len(sentence):
        if sentence[index + 1] == "a" and sentence[index + 2] == "t" and sentence[index + 3] == "e" and sentence[index + 4] == "r":
            words += 1
print(words)