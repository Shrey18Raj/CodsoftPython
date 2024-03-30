import tkinter as tk
from tkinter import messagebox

ENTRY_FONT = ("Arial", 12)
DEFAULT_FONT_STYLE = ("Arial", 20, 'bold')
WHITE = "#FFFFFF"
LIGHT_BLUE = "#5BC7F4"
LIGHT_GREEN = "#1BE65D"
RED = "#C40832"
LABEL_COLOUR = "#000000"
class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        self.tasks = []
        
        # Create task entry widget
        self.task_entry = tk.Entry(master, width=40, borderwidth=0, font=ENTRY_FONT)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)
        
        # Create add task button
        self.add_button = tk.Button(master, text="Add Task", bg=LIGHT_BLUE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)
        
        # Create listbox to display tasks
        self.task_listbox = tk.Listbox(master, width=50, borderwidth=0, font=ENTRY_FONT)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)
        
        # Create mark as completed button
        self.complete_button = tk.Button(master, text="Mark as Completed", bg=LIGHT_GREEN, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NSEW)
        
        # Create remove task button
        self.remove_button = tk.Button(master, text="Remove Task", bg=RED, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.remove_task)
        self.remove_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.NSEW)
        
        # Populate task listbox with existing tasks
        self.populate_task_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            task = self.task_listbox.get(task_index)
            self.task_listbox.delete(task_index)
            self.tasks.remove(task)
            self.task_listbox.insert(tk.END, f"{task}   ✔")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed!")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
        else:
            messagebox.showwarning("Warning", "Please select a task to remove!")

    def populate_task_listbox(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()