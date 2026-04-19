import tkinter as tk
from tkinter import scrolledtext
from rules import rules_list
from google import genai # pip install google-genai
from PIL import ImageTk, Image # pip install pillow
import json

client = genai.Client()

emotionImages = {}

def print_message(text, tag="response"):
    response_scrolledtext.config(state="normal")
    response_scrolledtext.insert(tk.END, f"{text}\n\n", tag)
    response_scrolledtext.config(state="disabled")
    response_scrolledtext.see(tk.END)

def load_image(path, size=(100,100)):
    img = Image.open(path) \
        .resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

def load_emotions():
    global emotionImages
    emotionImages = {
        "normal": load_image("images/normal.png", (100, 80)),
        "interest": load_image("images/interest.png"),
    }

def change_emotion(emotion):
    response_label.config(image=emotionImages[emotion])

def onclick(event=None):
    try:
        user_prompt = prompt_entry.get()

        if len(user_prompt) == 0: return
        print_message(user_prompt, "prompt")
        prompt_entry.delete(0, tk.END)

        prompt = (f"Оброби запит користувача: {user_prompt}.\n"
                 f"При формуванні відповіді слідуй наступним правилам: \n"
                  f"{'\n'.join(rules_list)}\n"
                  f"Доступні такі емоції: {','.join(emotionImages.keys())}\n")

        # Доступні моделі:
        # - gemini-3-flash-preview
        # - gemini-2.5-flash

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        print("\n")
        # response_text = str(response.text)
        response_json = json.loads(
            str(response.text).removeprefix("```json") \
                .removesuffix("```")
        )
        answer, emotion = response_json["answer"], response_json["emotion"]

        print_message(answer, "response")
        change_emotion(emotion)
    except Exception as error:
        # print(error)
        print_message(error, "error")


window = tk.Tk()
window.title("Візуальний асистент")
window.geometry("300x400")

# -- Верхня частина вікна
response_label = tk.Label()
response_label.pack()
load_emotions()
change_emotion("interest")

response_scrolledtext = scrolledtext.ScrolledText(height=15, wrap=tk.WORD,
                                                  state=tk.DISABLED)
response_scrolledtext.pack(fill="both", expand=True)
response_scrolledtext.tag_config("prompt", foreground="green", justify="right")
response_scrolledtext.tag_config("response", foreground="gray", justify="left")
response_scrolledtext.tag_config("error", foreground="red", justify="left")

# -- Нижня частина вікна
prompt_btn = tk.Button(text="Відправити", command=onclick)
prompt_btn.pack(side="bottom",fill="x")

prompt_entry = tk.Entry()
prompt_entry.pack(side="bottom", fill="x")
prompt_entry.bind("<Return>", onclick)

window.mainloop()
