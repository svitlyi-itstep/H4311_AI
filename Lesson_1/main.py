from google import genai
from rich.console import Console
from rich.markdown import Markdown
from colorama import just_fix_windows_console
from rules import rules_list

just_fix_windows_console()
console = Console()
client = genai.Client()

print(" — ШІ-асистента запущено!\n")
while True:
    user_prompt = input(" Введіть свій запит: ")

    if user_prompt.lower() in ["exit", "quit", "stop"]:
        break

    prompt = (f"Оброби запит користувача: {user_prompt}.\n"
             f"При формуванні відповіді слідуй наступним правилам: \n"
              f"{'\n'.join(rules_list)}")

    # Доступні моделі:
    # - gemini-3-flash-preview
    # - gemini-2.5-flash

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    print("\n")
    # print(response.text)
    console.print(
        Markdown(str(response.text))
    )

'''

    Зробити так, щоб після отримання відповіді від асистента на запит користувач
    міг одразу ввести новий запит. Так має продовжуватися до тих пір, доки користувач
    не введе стоп-слово (наприклад, exit).

'''