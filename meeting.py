#print("Welcome to dark world, creating of night!")

import tkinter as tk

def ntm():
    inf = entry.get()
    label.config(text=f"Welcome to judgment, {inf}")

root = tk.Tk()
root.title("Hello")

label = tk.Label(root, text="Welcome to dark world, creating of night! Whisper your name..")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="So my Name", command=ntm)
button.pack()

root.mainloop()

