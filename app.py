import os
import streamlit as st
from gtts import gTTS
from playsound import playsound
from recognizer import recognize_speech
from language_model import generate_response
from order_manager import handle_order
import pandas as pd


menu = pd.read_csv('menu_data.csv')


def main():
    st.title("KFC Voice-Activated Order Assistant")
    st.write("Welcome to KFC! Please place your order using the voice input button below.")


    st.sidebar.title("Menu")
    st.sidebar.dataframe(menu)

    if st.button("Record Order"):
        st.write("Listening...")
        order_text = recognize_speech()
        st.write(f"Recognized: {order_text}")

        if order_text:
            response = handle_order(order_text)
            st.write(response)
            tts = gTTS(text=response, lang='en')
            tts.save("response.mp3")
            playsound("response.mp3")
            os.remove("response.mp3")

            if order_text.lower() in ["stop", "no"]:
                st.write("Order process stopped.")
                return


if __name__ == "__main__":
    main()
