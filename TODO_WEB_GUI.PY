import streamlit as st
import TODO_FUNCTIONS as fn

todos = fn.get_todos()
def add_todo():
    new_todo = st.session_state["todo"] + "\n"
    todos.append(new_todo)
    fn.write_todos(todos)
    st.session_state["todo"] = ""  # Clear the value of the text input

st.title("My To-Do App")

st.write("This app is to increase your productivity.")

# Generate the list of todos
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # Edit button
        if st.button("Edit", key=f"Edit{index}"):
            st.session_state["edit_clicked"] = True
            st.session_state["selected_todo"] = todo
        # Complete button
        if st.button("Complete", key=f"Complete{index}"):
            st.session_state["complete_clicked"] = True
            st.session_state["selected_todo"] = todo

# Handle edit action
if "edit_clicked" in st.session_state and st.session_state["edit_clicked"]:
    # Find the index of the selected todo
    todo_index = todos.index(st.session_state["selected_todo"])
    new_todo = st.text_input("Rename todo", value=st.session_state["selected_todo"])
    if st.button("Confirm rename"):
        todos[todo_index] = new_todo + "\n"
        fn.write_todos(todos)  
        st.session_state["edit_clicked"] = False  
        st.rerun()  


if "complete_clicked" in st.session_state and st.session_state["complete_clicked"]:
    # Find the index of the selected todo
    todo_index = todos.index(st.session_state["selected_todo"])
    # Remove the to-do item from the list
    todos.pop(todo_index)
    # Update the todos in your storage mechanism (e.g., file)
    fn.write_todos(todos)
    # Reset the state
    st.session_state["complete_clicked"] = False
    # Optionally, you might want to remove the 'selected_todo' from the session state as well
    del st.session_state["selected_todo"]
    st.rerun()  



st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="todo")

st.session_state 