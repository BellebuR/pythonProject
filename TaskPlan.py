import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, bg="slate blue")


root = tk.Tk()
root.title("Task list")
root.configure(background="HotPink")

text1 = tk.Label(root, text="Input your task:", bg="HotPink")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="DeepPink1")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add task", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete task", command=delete_task)
delete_task_button.pack(pady=5)

mark_button = tk.Button(root, text="Task done", command=mark_task)
mark_button.pack(pady=5)

text2 = tk.Label(root, text="List of task:", bg="HotPink")
text2.pack(pady=5)
task_listbox = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_listbox.pack(pady=10)

root.mainloop()