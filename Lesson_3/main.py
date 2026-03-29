from google import genai # pip install google-genai
from rich.console import Console # pip install rich
from rich.markdown import Markdown
from colorama import just_fix_windows_console # pip install colorama
from rules import rules_list
import os, json

just_fix_windows_console()
console = Console()
client = genai.Client()

user = {
    "name": "",
    "age": 0
}
USER_INFO_FILE_PATH = "user_info.json"

def get_user_from_file():
    if os.path.exists(USER_INFO_FILE_PATH):
        with open(USER_INFO_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    return None

def get_user_from_console():
    info = {
        "name": input("Введіть своє ім'я: "),
        "age": int(input("Введіть свій вік: ")),
    }
    save_user(info)
    return info

def save_user(user_info):
    with open(USER_INFO_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(user_info, file)

def get_json(response):
    return json.loads(
        str(response.text).removeprefix("```json") \
        .removesuffix("```")
    )

print(" — ШІ-асистента запущено!\n")
if os.path.exists(USER_INFO_FILE_PATH):
    user = get_user_from_file()
else:
    user = get_user_from_console()

while True:
    user_prompt = input(" Введіть свій запит: ")

    if user_prompt.lower() in ["exit", "quit", "stop"]:
        break

    prompt = (f"Оброби запит користувача: {user_prompt}.\n"
             f"При формуванні відповіді слідуй наступним правилам: \n"
              f"{'\n'.join(rules_list)}"
              f"Інформація про користувача: {user}")

    # Доступні моделі:
    # - gemini-3-flash-preview
    # - gemini-2.5-flash

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print("\n")
    response_json = get_json(response)
    # print(response_text)
    # Виведення відповіді для користувача
    console.print(
        Markdown(response_json["answer"])
    )
    # Збереження оновленої інформації про користувача
    user = response_json["user"]
    save_user(user)

