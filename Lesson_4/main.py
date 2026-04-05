import tkinter as tk
from rules import rules_list
from google import genai # pip install google-genai

client = genai.Client()

def onclick():
    user_prompt = prompt_entry.get()

    if len(user_prompt) == 0: return

    prompt = (f"Оброби запит користувача: {user_prompt}.\n"
             f"При формуванні відповіді слідуй наступним правилам: \n"
              f"{'\n'.join(rules_list)}")

    # Доступні моделі:
    # - gemini-3-flash-preview
    # - gemini-2.5-flash

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print("\n")
    response_text = str(response.text)
    response_label.config(text=response_text)


window = tk.Tk()
window.title("Візуальний асистент")
window.geometry("300x400")

# -- Верхня частина вікна
response_label = tk.Label(text="Response")
response_label.pack()

# -- Нижня частина вікна
prompt_btn = tk.Button(text="Відправити", command=onclick)
prompt_btn.pack(side="bottom",fill="x")

prompt_entry = tk.Entry()
prompt_entry.pack(side="bottom", fill="x")

window.mainloop()
