from typing import List
import TODO_FUNCTIONS as fn    
import time  
import PySimpleGUI as sg
import os
import sys


# Get the directory of the executable
current_dir = os.path.dirname(os.path.abspath(sys.executable))

# Use the absolute path to 'todos.txt'
todos_file = os.path.join(current_dir, 'todos.txt')

# Create 'todos.txt' if it does not exist
if not os.path.exists(todos_file):
    with open(todos_file, 'w') as file:
        pass

with open(todos_file, 'r') as file:
    todos = file.readlines()

with open(todos_file, 'r') as file:
    todos = file.readlines()
    
sg.theme("Black")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    "My To-Do App",
    layout=[[clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]],
        font=("Helvetica", 15))


while True:
    event,values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todo = values["todo"] + "\n"
            todos = fn.get_todos()
            todos.append(todo)
            fn.write_todos(todos)  # Write todos to file
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todos = fn.get_todos()
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fn.write_todos(todos)  
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = fn.get_todos()
                todos.remove(todo_to_complete)
                fn.write_todos(todos)  # Write todos to file
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))
        case "Exit":
            todos = fn.get_todos()
            fn.write_todos(todos)  # Write todos to file before exiting
            break
        case "todos":
            try:
                window["todo"].update(value=values["todos"][0])
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))
        case sg.WIN_CLOSED:
            todos = fn.get_todos()
            fn.write_todos(todos)  # Write todos to file before closing
            break   
