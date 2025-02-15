import streamlit as st
from streamlit import session_state

from functions import write_todos, get_todos

todos = get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    write_todos(todos)

st.title('My todo app')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')