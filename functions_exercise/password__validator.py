def password_validator(password):
    invalid_password = []

    if not 6 <= len(password) <= 10:
        invalid_password.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        invalid_password.append("Password must consist only of letters and digits")

    if sum(char.isdigit() for char in password) < 2:
        invalid_password.append("Password must have at least 2 digits")

    if invalid_password:
        for errors in invalid_password:
            print(errors)
    else:
        print("Password is valid")


password_input = input()
password_validator(password_input)
