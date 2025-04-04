# Users dictionary to store user data
users = {}

def register_user():
    username = input("Enter your username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter your password: ")
    users[username] = {'password': [hash_password(password)], 'posts': []}
    print("Registration successful!")

def login_user():
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found.")
        return None
    password = input("Enter your password: ")
    if verify_password(password, users[username]['password'][-1]):
        print("Login successful!")
        return username
    print("Incorrect password.")
    return None
