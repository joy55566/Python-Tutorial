import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")
        self.root.geometry("400x500")
        
        # Task list
        self.tasks = []
        
        # Create GUI elements
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(root, width=40, height=15)
        self.task_listbox.pack(pady=10)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            self.tasks.pop(index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def mark_complete(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            if not task["completed"]:
                task["completed"] = True
                self.task_listbox.itemconfig(index, fg="green")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
