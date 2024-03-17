from getpass import getpass

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    pnumber  = input("Enter your phone number: ")
    name     = input("Enter your name: ")

    if username == "admin" and password == "12345" and pnumber == "123456" and name == "Nimo":
        print("Login successful!")
        print("welcome Nima")
    else:
        print("Invalid username or password.")
              
login()
