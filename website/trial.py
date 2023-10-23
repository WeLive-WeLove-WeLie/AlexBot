import streamlit as st
import random
import time

st.title("AlexBot")

BOT_NAME = "AlexBot"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

     # Add user message to chat history   
    st.session_state.messages.append({"role": "user", "content": prompt})


    # Display bot message in chat message container
    botmsg = "I'm good, thanks!" # Add your bot response here
    with st.chat_message('assistant'):
        st.markdown("I'm good, thanks!")
    
    # Add bot message to chat history
    st.session_state.messages.append({"role": 'assistant', "content": botmsg})



