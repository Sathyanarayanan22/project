def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password

def change_password(username, users):
    current_password = input("Enter your current password: ")
    if not verify_password(current_password, users[username]['password'][-1]):
        print("Incorrect current password.")
        return
    new_password = input("Enter new password: ")
    hashed_new = hash_password(new_password)
    if hashed_new in users[username]['password']:
        print("You can't use any of the last 3 passwords.")
        return
    users[username]['password'].append(hashed_new)
    if len(users[username]['password']) > 3:
        users[username]['password'].pop(0)
    print("Password changed successfully!")