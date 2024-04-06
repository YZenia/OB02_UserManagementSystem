class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        if not any(u.get_id() == user.get_id() for u in self._users):
            self._users.append(user)
            print(f"User {user.get_name()} added successfully.")
        else:
            print("A user with this ID already exists.")

    def remove_user(self, user_id):
        for i, user in enumerate(self._users):
            if user.get_id() == user_id:
                del self._users[i]
                print(f"User with ID {user_id} removed successfully.")
                return
        print("User not found.")

    def list_users(self):
        print("List of Users:")
        for user in self._users:
            print(f"ID: {user.get_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")


# Создание администратора и пользователей
admin = Admin(1, "Admin Name")
user1 = User(2, "User One")
user2 = User(3, "User Two")
user3 = User(4, "User Three")
user4 = User(5, "User Four")

# Добавление пользователей системой администратора
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)

# Просмотр списка пользователей
admin.list_users()

# Удаление пользователя
admin.remove_user(3)  # Удаление User Two

# Повторный просмотр списка пользователей
admin.list_users()
