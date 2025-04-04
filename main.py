def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. View Posts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                while True:
                    print("\nUser Menu:")
                    print("1. Change Password")
                    print("2. Post Content")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == "1":
                        change_password(username, users)
                    elif user_choice == "2":
                        post_content(username, users)
                    elif user_choice == "3":
                        break
        elif choice == "3":
            view_posts()
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()