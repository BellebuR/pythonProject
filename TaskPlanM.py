import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Планировщик задач")

        # Создание досок
        self.task_board = self.create_board("Задача", 0)
        self.in_progress_board = self.create_board("Выполняется", 1)
        self.completed_board = self.create_board("Выполненные", 2)

        # Поле для ввода новой задачи
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        # Кнопка для добавления новой задачи
        self.add_task_button = tk.Button(self.root, text="Добавить задачу", command=self.add_task)
        self.add_task_button.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

    def create_board(self, title, column):
        frame = tk.LabelFrame(self.root, text=title, padx=10, pady=10)
        frame.grid(row=0, column=column, padx=10, pady=10)
        listbox = tk.Listbox(frame, width=30, height=15)
        listbox.pack()
        listbox.bind("<Double-1>", self.move_task)
        return listbox

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_board.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Предупреждение", "Введите задачу перед добавлением.")

    def move_task(self, event):
        listbox = event.widget
        selected_task_index = listbox.curselection()

        if selected_task_index:
            task = listbox.get(selected_task_index)
            listbox.delete(selected_task_index)

            if listbox == self.task_board:
                self.in_progress_board.insert(tk.END, task)
            elif listbox == self.in_progress_board:
                self.completed_board.insert(tk.END, task)
            elif listbox == self.completed_board:
                self.completed_board.delete(selected_task_index)
        else:
            messagebox.showwarning("Предупреждение", "Выберите задачу для перемещения.")


if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()
task_listbox2 = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_listbox2.pack(pady=0)

root.mainloop()