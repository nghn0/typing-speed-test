import tkinter as tk
from tkinter import messagebox

paragraph = [
    [
        "The sun set behind the mountains casting a warm golden glow over the valley Birds chirped merrily returning "
        "to their nests after a long day Children laughed and played in the distance their silhouettes dancing in the "
        "fading light A gentle breeze rustled the leaves bringing with it the scent of blooming flowers Inside the "
        "cozy cabin a fire crackled in the hearth filling the room with a comforting warmth An old rocking chair "
        "creaked as it moved back and forth its occupant lost in thought The aroma of freshly baked bread wafted "
        "through the air making mouths water Outside the night sky was dotted with stars twinkling like distant "
        "diamonds"
    ]
]

timer = None
loc = None


def para_info():
    para_text.config(state=tk.NORMAL)
    para_text.insert(tk.END, paragraph[0][0])
    para_text.config(state=tk.DISABLED)


def start():
    type_text.grid(row=0, column=0)
    start_button.grid(row=1, column=0)
    start_button.config(text="Stop", command=stop)
    type_text.config(state=tk.NORMAL)
    type_text.delete("1.0", tk.END)
    typing()


def stop():
    root.after_cancel(timer)
    messagebox.showinfo("Time", "Time has stopped")
    type_text.config(state=tk.DISABLED)
    start_button.config(text="Start", command=start)
    check(type_text.get("1.0", tk.END))


def typing():
    global timer
    timer = root.after(62000, stop)


def check(string):
    correct = 0
    incorrect = 0
    total = 0
    inc = 0
    par = paragraph[0][0].split()
    string = string.split()
    for i in range(0, len(string)):
        for j in string[i]:
            try:
                if j == par[i][inc]:
                    correct = correct + 1
                    inc = inc + 1
                else:
                    incorrect = incorrect + 1
                    inc = inc + 1
            except IndexError:
                incorrect = incorrect + 1
                total = total - 1
            total = total + 1
        inc = 0

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0",
                       f"CPM: {correct}\nWPM: {int(correct / 5)}\nIncorrect Characters: {incorrect}\nAccuracy: {(correct / total) * 100}%")
    result_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Typing-Speed test")

para = tk.LabelFrame(root, text="Paragrapgh", pady=10, padx=10)

para_text = tk.Text(para, height=10, width=70, state=tk.DISABLED, font=("Arial", 19), wrap=tk.WORD)
para_info()
para_text.grid(row=0, column=0)

para.grid(row=0, column=0)

result = tk.LabelFrame(root, text="Result", pady=10, padx=10)

result_text = tk.Text(result, height=17, width=40, state=tk.DISABLED)
result_text.grid(row=0, column=0)

result.grid(row=0, column=1)

type = tk.LabelFrame(root, text="Type", padx=10, pady=10)

start_button = tk.Button(type, text="Start", command=start)
start_button.grid(row=0, column=0)

type_text = tk.Text(type, height=15, width=110, font=("Arial", 19), state=tk.DISABLED, wrap=tk.WORD)

type.grid(row=1, column=0, columnspan=2)
root.mainloop()
