import streamlit as st
import random
import pandas as pd
from scraper import *
from model import *
import json

old_prompt = json.loads(open('config.json').read())["old_prompt"]


st.title("AlexBot")

BOT_NAME = "AlexBot"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []





def send_model(button):
    st.session_state.messages.append({"role": "user", "content": button})
    if button=="specifications":
        

    else:
        product_details = json.loads(open('product/product_details.json').read())
        st.session_state.messages.append({"role": "assistant", "content": product_details[button]})

prompt = ""
st.sidebar.header("Link of the product")

prompt = st.sidebar.text_input("Enter the link of the product",prompt)

if prompt != "" :
    if old_prompt!= prompt:

        print("hello")
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": "New link detected. Please wait while we fetch the details."})
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
        main(link_to_product)
        st.session_state.messages.append({"role": "assistant", "content": "Details fetched. Please select the option you want to know about."})
        old_prompt = prompt
        # save this to config.json
        with open('config.json', 'w') as f:
            json.dump({"old_prompt": prompt}, f)
    # Display chat messages from history on app rerun

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # with st.chat_message("user"):
        # st.markdown(prompt)

    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": prompt})


    # #
    # # # getting the initial options for user
    product_details = json.loads(open('product/product_details.json').read())
    # # get all the keys
    # print(product_details.keys())
    for i in product_details.keys():
        st.button(i,on_click = send_model, args = (i,flag,f2))
else:
    with st.chat_message("assistant"):
        st.markdown("Please enter the link of the product.")





















# Display bot message in chat message container
# botmsg = "I'm good, thanks!"  # Add your bot response here
# with st.chat_message('assistant'):
#     st.markdown("I'm good, thanks!")
#
# # Add bot message to chat history
# st.session_state.messages.append({"role": 'assistant', "content": botmsg})

