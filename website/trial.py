import streamlit as st

st.title("Streamlit Trial")
# streamlit chat message
import streamlit as st
import numpy as np

with st.chat_message("user"):
    st.write("BHOSIKA")
prompt = st.chat_input("Say something")
if prompt:
    #chnage colour of the icon


    with st.chat_message("user"):
        st.write(prompt)
