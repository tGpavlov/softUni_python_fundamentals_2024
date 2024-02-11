year = int(input())

while True:
    year += 1
    year_as_string = str(year)
    digit_sum = ''
    is_happy_year = True
    for digit in year_as_string:
        if digit in digit_sum:
            is_happy_year = False
            break
        digit_sum += digit
    if is_happy_year:
        print(year)
        break

