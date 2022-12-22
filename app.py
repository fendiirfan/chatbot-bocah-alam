import streamlit as st
import requests
import time
from PIL import Image

def chatGPT(text):
  url = st.secrets["api_url"]
  headers = {
  "Content-Type": "application/json",
  "Authorization": st.secrets["chatgpt_token"],
  }
  data = { 
  "model": "text-davinci-003",
  "prompt": text,
  "max_tokens": 4000,
  "temperature": 1.0,
  }
  response = requests.post(url, headers=headers, json=data)
  output = response.json()['choices'][0]['text']
  
  return output

st.title('ChatBot E-Commerce Bocah Alam')
st.text("")
st.text("")

image = Image.open('Logo.png')

st.image(image,width=100,)
st.text("")

# inputan user
user_input = st.text_input('what can I do for you?')

# tombols
button = st.button('Send')

invalidInput = (len(user_input) <= 3 or
                len(user_input.split(' ')) > 200)

if button==True:
    if invalidInput:
        st.write('Please Input the Correct Sentence')
    else:
        with st.spinner('Wait for it...'):
          st.write(chatGPT(user_input))        
