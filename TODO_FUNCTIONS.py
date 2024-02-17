from typing import List
import os

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Use the absolute path to 'todos.txt'
todos_file = os.path.join(current_dir, 'todos.txt')

with open(todos_file, 'r') as file:
    todos = file.readlines()

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.txt")
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        pass

def get_todos(file_path="todos.txt"):
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines() 
    return todos_local

def write_todos(todos_arg, file_path="todos.txt"):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)

def print_todos(todos):
    for number, todo in enumerate(todos):
        row = f"{number + 1}-{todo.strip()}"
        print(row)


if __name__ == "__main__":
    print("This is the functions.py file.")
    print("It's used by main.py to test its functions.")
    print_todos(get_todos())