import streamlit as st
import requests

def chatBot(text):
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
  output = response.json()
  
  return output
