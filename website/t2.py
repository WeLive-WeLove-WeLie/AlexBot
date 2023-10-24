import streamlit as st
st.set_page_config(layout="wide")
with st.form(key='columns_in_form'):
    c1, c2 = st.columns((1,2))
    with c1:
        initialInvestment = st.text_input("Link of the product",value=500)
    with c2:
        monthlyContribution = st.text_input("Queries",value=100)

    submitButton = st.form_submit_button(label = 'Calculate')
    if submitButton:
        # disable the button so that it cannot be clicked again
        initialInvestment