import requests  # pip install requests
import os
import json

params = {
    "count": 0,
    "lang": ""
}

FILE_PATH = "meow_params.json"

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        params = json.load(file)
    if input(f"Ви хочете отримати {params['count']} фактів {params['lang']} мовою?").lower() == 'ні':
        params['count'] = int(input("Скільки фактів про котів вивести: "))
        params['lang'] = input("Якою мовою отримати факти? (ukr, eng, ger): ")
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(params, file)
else:
    params['count'] = int(input("Скільки фактів про котів вивести: "))
    params['lang'] = input("Якою мовою отримати факти? (ukr, eng, ger): ")
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(params, file)

url = f"https://meowfacts.herokuapp.com/"
response = requests.get(url, params)

if response.ok:
    # print(response.text)
    facts = response.json()['data']
    print("Випадкові факти про котів: ")
    for fact in facts:
        print(f" — {fact}")
else:
    response.raise_for_status()