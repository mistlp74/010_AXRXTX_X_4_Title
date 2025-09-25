from flask import Flask, render_template, request, redirect, url_for, render_template_string
from FileManager import load_users, create_user
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", page="home")


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users = load_users()

        if username in users:
            print("The user already exists")
            error = "User already exists"
            return render_template("signup.html", error=error, page="signup")

        create_user(username, password)

        success = f"User {username} successfully created"
        return render_template("home.html", success=success, page="signup")

    else:
        return render_template("signup.html", page="signup")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()

        # Перевірка в users.json
        if username in users and users[username]['password'] == password:
            return redirect(url_for('home'))
        else:
            error = 'Incorrect username or password'
            return render_template("login.html", error=error, page="login")

    return render_template("login.html", page="login")


@app.route('/profile')
def profile():
    return render_template("profile.html", page="profile")


if __name__ == '__main__':
    app.run(debug=True)
