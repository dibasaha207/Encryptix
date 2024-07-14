import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_tasks = task_list.curselection()
    for i in reversed(selected_tasks):
        task_list.delete(i)

root = tk.Tk()
root.config(bg='teal')
root.geometry('340x400')
root.resizable(False, False)
root.title("To Do List")

bar = tk.Frame(root, bg="white", height=50)
bar.pack(fill=tk.X)

text = tk.Label(bar, text="To Do List", bg='white', font=('arial', 16, 'bold'), fg='teal')
text.pack(pady=6)

entry = tk.Entry(root, width=30, background="white", foreground="black", font=("arial", 16))
entry.pack(pady=10, padx=7)

buttons_frame = tk.Frame(root, bg='teal')
buttons_frame.pack(pady=5)

add_button = tk.Button(buttons_frame, text="Add Task", width=10, command=add_task, background="white", fg="teal", borderwidth=3)
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = tk.Button(buttons_frame, text="Remove Task", width=10, command=remove_task, background="white", fg="teal", borderwidth=3)
remove_button.grid(row=0, column=1, padx=5, pady=5)

task_list = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("arial", 16))
task_list.pack(fill="both", expand=True, padx=7, pady=5)

root.mainloop()
