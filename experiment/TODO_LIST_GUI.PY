# main.py

import tkinter as tk
from tkinter import simpledialog, messagebox, END
import functions as fn

def add_todo(event=None):
    todo = todo_entry.get().capitalize()
    if todo.strip():
        todos.append(todo + "\n")
        update_todo_listbox()
        fn.write_todos(todos)
        todo_entry.delete(0, END)

def update_todo_listbox():
    todos_listbox.delete(0, END)
    for todo in todos:
        todos_listbox.insert(END, todo.strip())

def complete_todo():
    try:
        index = todos_listbox.curselection()[0]
        # Strikethrough item to mark as complete
        todos_listbox.itemconfig(index, {'bg':'light grey', 'fg':'gray'})
        # Alternatively, remove the item or add it to a 'completed' list
        completed_todo = todos.pop(index)
        fn.write_todos(todos)
        messagebox.showinfo("Task Completed", f"The task '{completed_todo.strip()}' has been marked as complete.")
    except IndexError:
        messagebox.showerror("Error", "Please select a task to complete")

def edit_todo(event=None):
    try:
        index = todos_listbox.curselection()[0]
        initial_value = todos[index].strip()
        edited_value = simpledialog.askstring("Edit Todo", "Edit your todo:", initialvalue=initial_value)
        if edited_value is not None:
            todos[index] = edited_value + "\n"
            update_todo_listbox()
            fn.write_todos(todos)
    except IndexError:
        messagebox.showerror("Error", "Please select a task to edit")

def edit_button_action():
    edit_todo()

def clear_entry():
    todo_entry.delete(0, END)

# Initialize the main window
app = tk.Tk()
app.title("Todo List Application")

todos = fn.get_todos()

# GUI layout and widget setup
top_frame = tk.Frame(app)
top_frame.pack(pady=(10, 0), padx=10, fill=tk.X)

todo_label = tk.Label(top_frame, text="Type a new todo here:")
todo_label.pack(side=tk.LEFT, padx=(0, 10))

todo_entry = tk.Entry(top_frame)
todo_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
todo_entry.bind('<Return>', add_todo)

middle_frame = tk.Frame(app)
middle_frame.pack(pady=(5, 0), padx=10, fill=tk.X)

add_button = tk.Button(middle_frame, text="Add Todo", command=add_todo)
add_button.pack(side=tk.LEFT, padx=5)

edit_button = tk.Button(middle_frame, text="Edit Selected Todo", command=edit_button_action)
edit_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(middle_frame, text="Complete Selected Todo", command=complete_todo)
complete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(middle_frame, text="Clear", command=clear_entry)
clear_button.pack(side=tk.LEFT, padx=5)

bottom_frame = tk.Frame(app)
bottom_frame.pack(pady=(5, 10), padx=10, fill=tk.BOTH, expand=True)

todos_listbox = tk.Listbox(bottom_frame)
todos_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(bottom_frame, command=todos_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

todos_listbox.config(yscrollcommand=scrollbar.set)
todos_listbox.bind('<Double-1>', edit_todo)

update_todo_listbox()

app.mainloop()
