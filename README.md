# Voice-Activated-KFC-Order-Assistant

The voice-activated KFC order assistant aims to streamline the process of placing orders at KFC drive-in locations using voice commands.

## List of Installed Packages and Dependencies

### Audio Playback and Recording:
```bash
pip install playsound
pip install pyaudio
pip install pydub
```

### Speech Recognition and Text-to-Speech:
```bash
pip install SpeechRecognition
pip install gtts
```

### Web Framework:
```bash
pip install flask
pip install streamlit
```

### Natural Language Processing:
```bash
pip install transformers
pip install torch
```

### Data Handling:
```bash
pip install pandas
```

### Platform-specific Requirements (for macOS):
```bash
pip3 install PyObjC
```

### Model:
- GPT-2 model (provided by the `transformers` library)

These installations cover the necessary tools for audio processing, speech recognition, text-to-speech conversion, web server setup, natural language processing, and data handling.

## Run Your Application:

### Start the Flask API:
```bash
python api_server.py
```

### Run the main application:
```bash
python main.py
```

## Summary

The voice-activated KFC order assistant provides a seamless ordering experience through voice commands, leveraging natural language processing technologies.
```
