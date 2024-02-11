# words = input().split()
# palindrome = input()
#
# palindrome_list = [word for word in words if word == word[::-1]]
# palindrome_count = palindrome_list.count(palindrome)
#
# print(f'{palindrome_list}\nFound palindrome {palindrome_count} times')


strings = input().split()
searched_palindrome = input()
palindromes = []

for word in strings:
    if word == ''.join(reversed(word)):
        palindromes.append(word)

print(f'{palindromes}\nFound palindrome {palindromes.count(searched_palindrome)} times')
