import streamlit as st

text_input_container = st.empty()
t = text_input_container.text_input("Enter something")

if t != "":
    text_input_container.empty()
    st.write(t)