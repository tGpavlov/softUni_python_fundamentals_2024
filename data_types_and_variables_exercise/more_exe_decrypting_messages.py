key_num = int(input())
num_of_lines = int(input())
decrypted_message = ''
for current_letter in range(num_of_lines):
    letter = input()
    decrypted_message += chr(ord(letter) + key_num)
print(decrypted_message)
