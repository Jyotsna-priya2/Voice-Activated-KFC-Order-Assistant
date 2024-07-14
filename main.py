import os
from gtts import gTTS
from playsound import playsound
from recognizer import recognize_speech
from language_model import generate_response
from order_manager import handle_order

def main():
    while True:
        print("Welcome to KFC! Please place your order.")
        order_text = recognize_speech()

        if order_text:
            response = handle_order(order_text)
            print(response)

            tts = gTTS(text=response, lang='en')
            tts.save("response.mp3")
            playsound("response.mp3")
            os.remove("response.mp3")
        if ((order_text=="stop") or (order_text=="no")):
            break

if __name__ == "__main__":
    main()
