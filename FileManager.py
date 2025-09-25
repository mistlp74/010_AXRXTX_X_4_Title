import json
import random
from random import randint


def load_users():
    try:
        with open('data/users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print("users.json was loaded successfully")
            return data
    except:
        print("Error loading users.json")
        default_users = {
            "Username": {
                "password": "12345678"
            }
        }
        with open('data/users.json', 'w', encoding='utf-8') as file:
            json.dump(default_users, file, indent=2, ensure_ascii=False)
        return default_users

def create_user(username, password):
    data = load_users()
    data[username] = {"password": password}

    with open('data/users.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open('data/users.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)