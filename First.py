import tkinter as tk

root = tk.Tk()
root.title("Hello")

label = tk.label(root, text="Welcome to dark world, creating of night! Whisper your name..")
label.pack()

entry = tk,Entry(root)
entry.pack()

button = tk.Button(root, text="So my Name", command=entry)

root.mainloop()