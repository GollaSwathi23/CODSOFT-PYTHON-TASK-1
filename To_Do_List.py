import tkinter as tk
from tkinter import messagebox
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")
def edit_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_index)
        entry_task.delete(0, tk.END)
        entry_task.insert(tk.END, task)
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")
# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry('500x500')
# Create and position widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)
root.configure(bg="snow2")
# header_frame = tk.Frame(root, bg = "#FAEBD7")  
header_label = tk.Label(root,text = "The To-Do List",font = ("Brush Script MT", "30"),width=20,background = "white",foreground = "medium purple")  
header_label.pack(padx=20,pady=5)
listbox_tasks = tk.Listbox(root, width=25, height=25, font=("Consolas", "15", "bold"), selectmode='SINGLE', background="#FFFFFF", foreground="#000000", selectbackground="#CD853F", selectforeground="#FFFFFF")
listbox_tasks.place(x=250, y=100)
# scrollbar_tasks = tk.Scrollbar(frame_tasks)
# scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
# listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
# scrollbar_tasks.config(command=listbox_tasks.yview)
task = tk.Label(root, text="Enter Task:", font=("Consolas", "15", "bold"), width=20,background="green yellow", foreground="#000000").place(x=20, y=110)
# entry_task=tk.Entry(root,font=("Consolas", "12"), width=20).place(x=20, y=150)
entry_task = tk.Entry(root,font=("Consolas", "15", "bold"), width=18)
entry_task.pack(padx=20,pady=70,anchor="sw")
button_add_task = tk.Button(root,text="Add Task", width=24,background="purple1",command=add_task).place(x=30, y=200)
# button_add_task.pack(padx=30,pady=20)
button_delete_task = tk.Button(root, text="Delete Task",background="dark green",width=24, command=delete_task).place(x=30,y=250)
# button_delete_task.pack(padx=30,pady=250)
button_edit_task = tk.Button(root, text="Edit Task",background="pale violet red",width=24, command=edit_task).place(x=30,y=300)
# button_edit_task.pack(padx=30,pady=300)
# Start the main event loop
root.mainloop()
