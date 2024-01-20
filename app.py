from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get the response

model = genai.GenerativeModel("gemini-pro") ##for text use "gemini-pro"
def get_genini_response(question):
    response = model.generate_content(question)
    return response.text

## init streamlit app

st.set_page_config(page_title="Question & Answer Demo")
st.header("Gemini Pro LLM Appllication")

input = st.text_input("Input: ",key="input")
submit = st.button("Ask ther question")

## When submit button is clicked,  

if submit:
    response = get_genini_response(input)
    st.subheader("The response is")
    st.write(response)
    