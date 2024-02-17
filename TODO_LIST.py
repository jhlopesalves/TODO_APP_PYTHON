from typing import List
import TODO_FUNCTIONS as fn    
import time     
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

now = time.strftime("%b %d, %Y %H:%M:%S")
print (f"It is {now}")
while True:
    todos = fn.get_todos()
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()
    
    if user_action.startswith("add"):
        if len(user_action) > 4:
            todo = user_action[4:].capitalize() + "\n"  
        else:
            todo = input("Enter the task you want to add: ").capitalize() + "\n"
        todos.append(todo)
        fn.write_todos(todos)
        print("This is the current list of todos:")
        fn.print_todos(todos)
             
    elif user_action.startswith("show"):
        print("This is the current list of todos:")
        fn.print_todos(todos)
                
    elif user_action.startswith("edit"):
        print("This is the current list of todos, choose one to edit:")
        if todos is not None:
            fn.print_todos(todos)
            while True:
                number_input = input("Enter the number of the todo you want to edit: ")
                if number_input.isdigit():
                    number = int(number_input) - 1
                    fn.print_todos(todos)
                    if number >= 0 and number < len(todos):
                        todos[number] = input("Enter the new todo: ").capitalize() + "\n"
                        fn.write_todos(todos)
                        break
                    else:
                        print("Invalid number. Please try again.")

    elif user_action.startswith("complete"):
        print("This is the current list of todos, choose one to complete:")
        if todos is not None:
            fn.print_todos(todos)
            while True:
                number_input = input("Enter the number of the todo you want to complete: ")
                if number_input.isdigit():
                    number = int(number_input) - 1
                    if number >= 0 and number < len(todos):
                        todos.pop(number)
                        fn.write_todos(todos)
                        break
                    else:
                        print("Invalid number. Please try again.")
                else:
                    print("Invalid input. Please enter a number.")
        else:
            print("No todos found.")

    elif user_action.startswith("exit"):
        print("Goodbye!")
        break

    else:
        print("Command not recognized. Please try again.")

