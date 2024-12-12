import streamlit as st

def app():
    st.title("My Account")
    choice=st.selectbox('login or sign up',['login','sign up'])
    if choice=='login':
        email=st.text_input('Enter the Email Address')
        password=st.text_input('password',type='password')
        st.button('login')

    else:
        email=st.text_input('Enter the Email Address')
        password=st.text_input('password',type='password')
        username=st.text_input('Enter the unique username')
        st.button('Create My Account') 