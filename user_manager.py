class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username):
        if username not in self.users:
            self.users.append(username)
            return True
        return False

    def user_exists(self, username):
        return username in self.users

    def get_all_users(self):
        return self.users
