# Voice-Activated-KFC-Order-Assistant

The voice-activated KFC order assistant aims to streamline the process of placing orders at KFC drive-in locations using voice commands.

## Project Overview

This project uses a combination of Flask for the backend API and Streamlit for the frontend interface. It employs the GPT-2 model for natural language generation, allowing the system to handle various order inputs effectively. The project reads menu data from a CSV file and uses it to process orders and calculate the total cost.

## Features

- Voice recognition for order placement.
- Natural language processing using GPT-2.
- Real-time text-to-speech conversion.
- Interactive menu display via Streamlit.

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
These installations cover the necessary tools for audio processing, speech recognition, text-to-speech conversion, web server setup, natural language processing, and data handling.

### Model:
- GPT-2 model (provided by the `transformers` library)


## How It Works

### 1. Model Usage

The GPT-2 model from the `transformers` library generates responses based on user input. Here’s how it’s implemented:

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
```
**Where and Why It Is Used:**
- **Where:** In `language_model.py`.
- **Why:** To generate natural language responses to user inputs, providing a conversational experience.

### 2. CSV File Handling

Menu data is stored in a CSV file (`menu_data.csv`) and is read using `pandas`.

**How the CSV File Is Read and Used:**
- **Read:** The `menu_data.csv` file is read into a pandas DataFrame.
- **Use:** The DataFrame is used to look up item prices and calculate the total cost of the order.

### 3. Output Generation

The application captures voice inputs, processes them, and generates appropriate responses. The main logic is in `main.py`:

**Explanation:**
- **Voice Input:** Captures voice input from the user.
- **Text Conversion:** Converts voice input to text using `recognize_speech`.
- **Order Handling:** Processes the order using `handle_order`.
- **Response Generation:** Generates and plays a voice response using `gTTS`.


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
