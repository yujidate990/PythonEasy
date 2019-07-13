users = [
    {
        "id": 1,
        "name": "Taro",
        "age": 20
    },
    {
        "id": 2,
        "name": "Hanako",
        "age": 18
    },
    {
        "id": 3,
        "name": "Kubo",
        "age": 25
    }
]

def get_user(name):
    for user in users:
        if name == user["name"]:
            return user
    else:
        return None

