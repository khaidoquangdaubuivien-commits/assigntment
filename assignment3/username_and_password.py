attempt = 0
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "python" and password == "rules" :
        print("Welcome")
        break

    else:
        attempt = attempt + 1

        if attempt == 5:
            print("Access denied")
            break

        else:
            print("Wrong username or password")
        continue
