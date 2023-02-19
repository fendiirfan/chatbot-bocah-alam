import streamlit as st
from PIL import Image
from chatbot import chatBot

from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events



st.title('ChatBot E-Commerce Bocah Alam')
st.text("")
st.text("")

image = Image.open('Logo.png')

st.image(image,width=100,)
st.text("")
st.text("The E-Commerce Chatbot Bocah Alam is a demo chatbot made with state-of-the-art Artificial Intelligence models.\nYou can inquire about assistance and ask questions related to the environment and the Bocah Alam website.\nThis outstanding chatbot showcases the cutting-edge capabilities of AI technology.")
st.text("")


# inputan user
user_input = st.text_input('what can I do for you?')

# tombols
button = st.button('Send')


stt_button = Button(label="Speak", width=100)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result: # Speak
    if "GET_TEXT" in result:
        st.write("Your command : \n",result.get("GET_TEXT"))
        with st.spinner('Typing...'):
          st.markdown("ChatBot Response : \n")
          st.write(chatBot(result.get("GET_TEXT")))
elif button==True: # submit text input
    with st.spinner('Typing...'):
      st.markdown("ChatBot Response : \n")
      st.write(chatBot(user_input))  
