from flask import Flask, render_template, request, redirect, url_for
from FileManager import load_users_from_json
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", page="home")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    users = load_users_from_json()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            error = "Заповніть всі поля"
            return render_template("signup.html", error=error, page="signup")

        if username in users:
            error = f"Користувач {username} вже існує!"
            return render_template("signup.html", error=error, page="signup")

        users[username] = {
            "username": username,
            "password": password
        }

        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=2, ensure_ascii=False)

        success = f"Користувач {username} успішно створений!"
        return render_template("home.html", success=success, page="signup")

    return render_template("signup.html", page="signup")


@app.route('/login', methods=['GET', 'POST'])
def login():
    users = load_users_from_json()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Перевірка в users.json
        if username in users and users[username]['password'] == password:
            return redirect(url_for('home'))
        else:
            error = 'Невірний логін або пароль'
            return render_template("login.html", error=error, page="login")

    return render_template("login.html", page="login")


@app.route('/profile')
def profile():
    return render_template("profile.html", page="profile")


if __name__ == '__main__':
    app.run(debug=True)
