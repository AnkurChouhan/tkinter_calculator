import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    f = tk.Frame(button_frame)
    f.pack(expand=True, fill='both')
    for btn in row:
        b = tk.Button(f, text=btn, font='Arial 18', relief=tk.GROOVE)
        b.pack(side=tk.LEFT, expand=True, fill='both')
        b.bind('<Button-1>', click)

root.mainloop()
