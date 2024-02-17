import streamlit as st
import TODO_FUNCTIONS as fn

todos = fn.get_todos()
st.title("Todo App")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=i)
st.text_input(label="", placeholder="Add a new todo", key="todo")