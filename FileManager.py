import json

def load_users_from_json():
    try:
        with open('data/users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        print("loading users.json failed")

        default_users = {
            "User": {
                "username": "User",
                "password": "12345678",
            }
        }
        with open('data/users.json', 'w', encoding='utf-8') as file:
            json.dump(default_users, file, indent=2, ensure_ascii=False)
        return default_users