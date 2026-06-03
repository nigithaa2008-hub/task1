attempt = 0

while attempt < 3:
    name = input("enter the name: ")
    password = input("enter the password: ")

    if not name.isalpha() or not password.isdigit():
        print("Invalid input, try again")
        attempt += 1
    else:
        print("correct name")
        print("correct password")
        print("done")
        break

if attempt == 3:
    print("register cannot be done")