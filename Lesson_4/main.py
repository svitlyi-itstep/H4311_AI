import tkinter as tk
from tkinter import scrolledtext
from rules import rules_list
from google import genai # pip install google-genai

client = genai.Client()

def print_message(text, tag="response"):
    response_scrolledtext.config(state="normal")
    response_scrolledtext.insert(tk.END, f"{text}\n\n", tag)
    response_scrolledtext.config(state="disabled")
    response_scrolledtext.see(tk.END)

def onclick():
    try:
        user_prompt = prompt_entry.get()

        if len(user_prompt) == 0: return
        print_message(user_prompt, "prompt")
        prompt_entry.delete(0, tk.END)

        prompt = (f"Оброби запит користувача: {user_prompt}.\n"
                 f"При формуванні відповіді слідуй наступним правилам: \n"
                  f"{'\n'.join(rules_list)}")

        # Доступні моделі:
        # - gemini-3-flash-preview
        # - gemini-2.5-flash

        response = client.models.generate_content(
            model="gemini-2.6-flash",
            contents=prompt,
        )
        print("\n")
        response_text = str(response.text)
        print_message(response_text, "response")
    except Exception as error:
        print(error)


window = tk.Tk()
window.title("Візуальний асистент")
window.geometry("300x400")

# -- Верхня частина вікна
response_label = tk.Label(text="Response")
response_label.pack()

response_scrolledtext = scrolledtext.ScrolledText(height=20, wrap=tk.WORD,
                                                  state=tk.DISABLED)
response_scrolledtext.pack(fill="both", expand=True)
response_scrolledtext.tag_config("prompt", foreground="green", justify="right")
response_scrolledtext.tag_config("response", foreground="gray", justify="left")

# -- Нижня частина вікна
prompt_btn = tk.Button(text="Відправити", command=onclick)
prompt_btn.pack(side="bottom",fill="x")

prompt_entry = tk.Entry()
prompt_entry.pack(side="bottom", fill="x")

window.mainloop()
