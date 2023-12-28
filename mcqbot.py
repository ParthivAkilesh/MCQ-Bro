import streamlit as st
from PIL import Image
import google.generativeai as genai



genai.configure(api_key="AIzaSyA9-uT6c7ObCzclRwiHKytunvjTaiQixeY")



def get_gemini_response(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    
    response = model.generate_content(["What is the answer for the given MCQ?",image])
    return response.text


st.set_page_config(page_title="MCQ Bro")

with st.sidebar:

    st.header("I am your external-brain!!")

    input=st.text_input("Input Prompt: ",key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""  
    
    submit=st.button("GET ANSWER📤")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Question.", use_column_width=True)



if submit: 
    response=get_gemini_response(image)
    st.subheader("The Correct answer is...")
    st.success(response)