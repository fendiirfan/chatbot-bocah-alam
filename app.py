import streamlit as st
import requests
import time

def chatGPT(text):
  url = "https://api.openai.com/v1/completions"
  headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer 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",
  }
  data = { 
  "model": "text-davinci-003",
  "prompt": text,
  "max_tokens": 4000,
  "temperature": 1.0,
  }
  response = requests.post(url, headers=headers, json=data)
  output = response.json()['choices'][0]['text']
  
  return print(output)

def progressBar(my_bar,start,end):
    for percent_complete in range(start,end):
        time.sleep(0.1)
            
        my_bar.progress(percent_complete + 1)

st.title('Prototype ChatBot E-Commerce')
st.text("")
st.text("")

# inputan user
user_input = st.text_input('Input Sentence')

# tombols
button = st.button('Send')

invalidInput = (len(user_input) <= 3 or
                len(user_input.split(' ')) > 200)

if button==True:
    if invalidInput:
        st.write('Please Input the Correct Sentence')
    else:
        # DISPLAY LOADING PROGRESS FROM 0-20s
        my_bar = st.progress(0)

        progressBar(my_bar,0,20)
        
        response_text = chatGPT(user_input)

        # DISPLAY LOADING PROGRESS FROM 20-70
        progressBar(my_bar,20,70)
        
        # DISPLAY LOADING PROGRESS FROM 70-100
        progressBar(my_bar,70,100)
        
        # DISPLAY PREDICTION
        st.write(response_text)