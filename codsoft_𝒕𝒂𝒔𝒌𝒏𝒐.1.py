import csv
import tkinter as tk
from tkinter import messagebox

''' importing csv to store the tasks in a csv file
importing tkinter to create interactive user interface 
and from tkinter importing messagebox for displaying messages to the user'''

# creating class and using the special method __init__ to initialize the object.
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.load_tasks()

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack()

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

# load_tasks method for loading tasks from tasks.csv file and using listbox to show the tasks in list form.
    def load_tasks(self):
        with open("tasks.csv", "r") as file:
            reader = csv.reader(file)
            self.tasks = [row[0] for row in reader]
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)

# save_tasks method for saving tasks to tasks.csv file.
    def save_tasks(self):
        with open("tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task])

# add_task method for adding tasks to the listbox and saving them to tasks.csv file.
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

# delete_task method for deleting tasks from the listbox and saving them to tasks.csv file.
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
            self.save_tasks()

# main method for creating the GUI application.
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
