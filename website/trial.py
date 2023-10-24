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


def bool_f():
    with open('config.json', 'w') as f:
        json.dump({"bool": False,"old_prompt":old_prompt}, f)
def bool_t():
    with open('config.json', 'w') as f:
        json.dump({"bool": True,"old_prompt":old_prompt}, f)

def send_model(button):
    product_details = json.loads(open('product/product_details.json').read())
    st.session_state.messages.append({"role": "user", "content": button})
    if button=="specifications":
        st.session_state.messages.append({"role": "assistant", "content": "What is your question about specifications?"})
        bool_f()
    elif button=="review":
        reviews = json.loads(open('product/reviews.json').read())
        answer = get_response("summarize all the reviews", reviews)
        st.session_state.messages.append({"role": "assistant", "content": answer})
    else:
        product_details = json.loads(open('product/product_details.json').read())
        st.session_state.messages.append({"role": "assistant", "content": product_details[button]})

prompt = ""
st.sidebar.header("Link of the product")
rendered = False
prompt = st.sidebar.text_input("Enter the link of the product",prompt)
with open('config.json') as f:
    bool = json.load(f)["bool"]
if not bool:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    q = st.empty()
    if query := q.chat_input("Ask your query"):
        st.session_state.messages.append({"role": "user", "content": query})
        with open("product/product_details.json") as f:
            product_details = json.load(f)
        q.empty()
        with st.chat_message("user"):
            st.markdown("Question: "+query)
        answer = get_response(query, product_details["specifications"])
        st.session_state.messages.append({"role": "assistant", "content": answer})
        print(answer)
        with st.chat_message("assistant"):
            st.markdown("Answer: "+answer)
        bool_t()
        rendered = True



with open('config.json') as f:
    bool = json.load(f)["bool"]
if prompt != "" and bool  :

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
            json.dump({"old_prompt": prompt,"bool":bool}, f)
    # Display chat messages from history on app rerun
    if not rendered:
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
    # print(product_details.keys()
    for i in product_details.keys():
        st.button(i,on_click = send_model, args = (i,))
    st.button("Summary of the reviews",on_click = send_model, args = ("review",))
elif prompt == "" and bool:
    with st.chat_message("assistant"):
        st.markdown("Please enter the link of the product.")





















# Display bot message in chat message container
# botmsg = "I'm good, thanks!"  # Add your bot response here
# with st.chat_message('assistant'):
#     st.markdown("I'm good, thanks!")
#
# # Add bot message to chat history
# st.session_state.messages.append({"role": 'assistant', "content": botmsg})

