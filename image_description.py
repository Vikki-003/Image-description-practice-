import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os
import streamlit as st 

load_dotenv()
genai_api_key=os.getenv('GEMINI_API_KEY')
st.title('Image application')
path=st.file_uploader('upload image')
if path is not None:
    st.image(Image.open(path))
    
prompt=st.text_input('ask question you want')

if st.button('click'):
    img=Image.open(path)
    genai.configure(api_key=genai_api_key)
    model=genai.GenerativeModel('gemini-2.5-flash')
    response=model.generate_content([prompt,img])
    st.success(response.text)