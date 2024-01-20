from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get the response

model = genai.GenerativeModel("gemini-pro-vision") ##for image use "gemini-pro-vision"
def get_genini_response(input, image):
    if input !="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

## initialize streamlit application

st.set_page_config(page_title="Gemini Pro Image Demo")
st.header("Gemini Application")
input = st.text_input("Input Promt: ",key="input")

## Uploading the image 

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploadeded Image.", use_column_width = True)

submit = st.button("Tell me about the image")

#if submit is clicked

if submit:
    response = get_genini_response(input, image)
    st.subheader("The response is")
    st.write(response)

