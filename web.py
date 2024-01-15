import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] +'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("My todo list app")
st.subheader("This is my web app")
st.write("This is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter new todo...",
              on_change=add_todo, key='new_todo')

st.session_state