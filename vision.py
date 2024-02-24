from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(image)
    return response.text



st.set_page_config(page_title="Dadah AI", page_icon="🌌")

st.header("Dadah AI")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)


submit=st.button("Tell me about this image")


if submit:
    response=get_gemini_response(image)
    st.subheader("Dadah AI")
    st.write(response)
