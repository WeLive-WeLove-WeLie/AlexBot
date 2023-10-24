import streamlit as st
import random
import pandas as pd
from scraper import *
import json

st.title("AlexBot")

BOT_NAME = "AlexBot"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if 'keys' not in st.session_state:
    st.session_state.keys = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

for keys in st.session_state.keys:
    with st.button(keys["role"]):
        st.markdown(keys["content"])
# Accept user input
if prompt := st.chat_input("What is up?"):


    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # extracting the product link
    link = prompt[25:]
    link_to_product = []
    for i in link:
        if i == '?':
            break
        else:
            link_to_product.append(i)
    link_to_product = "".join(link_to_product)
    # print(link_to_product)
    # getting jsons from the scraper(scraper.py)
    # main(link_to_product)
    # #
    # # # getting the initial options for user
    # product_details = json.loads(open('product/product_details.json').read())
    keys = ["a","b","c"]
    # # get all the keys
    # print(product_details.keys())
    for i in keys:
        st.session_state.messages.append({"role": "bot", "content": i})
        st.button(i)






















    # Display bot message in chat message container
    # botmsg = "I'm good, thanks!"  # Add your bot response here
    # with st.chat_message('assistant'):
    #     st.markdown("I'm good, thanks!")
    #
    # # Add bot message to chat history
    # st.session_state.messages.append({"role": 'assistant', "content": botmsg})

