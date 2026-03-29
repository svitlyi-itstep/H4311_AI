import os
import json

user = {
    "name": "",
    "age": 0
}

FILE_PATH = "data.txt"

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        user = json.load(file)
else:
    user["name"] = input("Введіть своє ім'я: ")
    user["age"] = int(input("Введіть свій вік: "))

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(user, file)

print(f"Привіт, {user['name']}! Тобі {user['age']} років!")


'''

    Змінити асистента таким чином, щоб він запам'ятовував
    введене користувачем ім'я і не перепитував його після
    перезапуску програми.
    
    Для цього записувати ім'я користувача у файл і при запуску
    програми перевіряти наявність імені у файлі.

'''