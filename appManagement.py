from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# Пример списка пользователей и класса пользователя
class User:
    def __init__(self, user_id, name, access_level='user'):
        self.user_id = user_id
        self.name = name
        self.access_level = access_level

# Список пользователей
users = [User(1, "Администратор", 'admin'), User(2, "Пользователь 1")]

# HTML шаблон
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Система Управления Пользователями</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        form { margin-bottom: 20px; }
        input[type="text"], input[type="number"] { padding: 10px; margin-right: 10px; }
        input[type="submit"] { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        input[type="submit"]:hover { background-color: #45a049; }
    </style>
</head>
<body>

<h2>Система Управления Пользователями</h2>

<!-- Форма для добавления пользователя -->
<h3>Добавить пользователя:</h3>
<form action="/add_user" method="post">
    <label for="user_id">ID пользователя:</label>
    <input type="number" id="user_id" name="user_id" required>
    <label for="name">Имя:</label>
    <input type="text" id="name" name="name" required>
    <input type="submit" value="Добавить">
</form>

<!-- Форма для удаления пользователя -->
<h3>Удалить пользователя:</h3>
<form action="/remove_user" method="post">
    <label for="remove_user_id">ID пользователя:</label>
    <input type="number" id="remove_user_id" name="remove_user_id" required>
    <input type="submit" value="Удалить">
</form>

<!-- Таблица для отображения пользователей -->
<h3>Список пользователей:</h3>
<table>
    <tr>
        <th>ID пользователя</th>
        <th>Имя</th>
        <th>Уровень доступа</th>
    </tr>
    {% for user in users %}
    <tr>
        <td>{{ user.user_id }}</td>
        <td>{{ user.name }}</td>
        <td>{{ user.access_level }}</td>
    </tr>
    {% endfor %}
</table>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    user_id = request.form['user_id']
    name = request.form['name']
    # Проверка на уникальность ID
    if any(user.user_id == int(user_id) for user in users):
        return "Пользователь с таким ID уже существует.", 400
    new_user = User(int(user_id), name)
    users.append(new_user)
    return home()

@app.route('/remove_user', methods=['POST'])
def remove_user():
    user_id = int(request.form['remove_user_id'])
    # Поиск и удаление пользователя
    for i, user in enumerate(users):
        if user.user_id == user_id:
            users.pop(i)
            return home()
    return "Пользователь не найден.", 404

if __name__ == "__main__":
    app.run(debug=True)
