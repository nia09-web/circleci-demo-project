from user_manager import UserManager

if __name__ == "__main__":
    um = UserManager()

    while True:
        print("\nOptions:")
        print("1. Add user")
        print("2. List users")
        print("3. Check if user exists")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username to add: ")
            if um.add_user(username):
                print(f"✅ '{username}' added.")
            else:
                print(f"⚠️ '{username}' already exists.")

        elif choice == "2":
            print("👥 Users:", um.get_all_users())

        elif choice == "3":
            username = input("Enter username to check: ")
            if um.user_exists(username):
                print(f"✅ '{username}' exists.")
            else:
                print(f"❌ '{username}' does not exist.")

        elif choice == "4":
            print("👋 Exiting.")
            break
        else:
            print("Invalid choice. Please try again.") 
