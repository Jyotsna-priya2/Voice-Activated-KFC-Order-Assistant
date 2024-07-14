# Voice-Activated-KFC-Order-Assistant
The voice-activated KFC order assistant aims to streamline the process of placing orders at KFC drive-in locations using voice commands.
List of Installed Packages and Dependencies
Audio Playback and Recording:
pip install playsound
pip install pyaudio
pip install pydub
Speech Recognition and Text-to-Speech:
pip install SpeechRecognition:
pip install gtts
Web Framework
pip install flask
Natural Language Processing:
pip install transformers
pip install torch
Data Handling
pip install pandas
Platform-specific Requirements (for macOS):
pip3 install PyObjC
Model:
GPT-2 model (provided by the transformers library)
These installations cover the necessary tools for audio processing, speech recognition, text-to-speech conversion, web server setup, natural language processing, and data handling.


Run Your Application:
Start the Flask API: python api.py
Run the main application: python main.py




Voice-Activated KFC Order Assistant Documentation
Table of Contents
Introduction
Purpose
Scope
Audience
API Integration
Technologies Used
API Endpoints
Request and Response Formats
System Architecture
Overview
Components
Language Model (LLM) Implementation
Model Selection
Training Data
Preprocessing Steps
User Interaction Workflow
User Interface Design
Voice Recognition
Order Processing Logic
Error Handling
Deployment
Environment Setup
Deployment Steps
Testing Procedures
Maintenance and Updates
Conclusion
Summary
Future Enhancements











1. Introduction
Purpose
The voice-activated KFC order assistant aims to streamline the process of placing orders at KFC drive-in locations using voice commands.
Scope
This documentation covers the integration of voice recognition, natural language understanding, and API development for seamless order processing.
Audience
Developers
Project Managers
Stakeholders
2. API Integration
Technologies Used
Python
Flask
SpeechRecognition
Transformers (Hugging Face)
Pandas
API Endpoints
/get_menu: Retrieves the current menu items and prices.
/place_order: Accepts order requests and calculates the total cost.
Request and Response Formats
JSON format for both requests and responses.
Example:
json
Copy code
{
  "order": ["family deal", "classic zinger"]
}


3. System Architecture
Overview
The system consists of a Flask-based API server that integrates a language model for understanding user orders and processing them against a predefined menu.
Components
API Server: Handles incoming requests and communicates with the language model.
Language Model: Uses Hugging Face's transformers library to process natural language and generate responses.
4. Language Model (LLM) Implementation
Model Selection
GPT-2: Chosen for its ability to generate coherent text based on input prompts.
Training Data
Utilizes pre-trained weights and fine-tuning on specific restaurant order datasets.
Preprocessing Steps
Tokenization of input text using GPT-2 tokenizer.
5. User Interaction Workflow
User Interface Design
Voice-driven interface with speech recognition for input.
Audio feedback using gTTS for response output.
Voice Recognition
Utilizes the SpeechRecognition library to convert speech to text.
Order Processing Logic
Matches user input against the menu items to compute the total cost.
Handles special requests and additional items.
Error Handling
Recognizes and handles unrecognized inputs gracefully.
Provides clear prompts for user actions.
6. Deployment
Environment Setup
Python virtual environment with required libraries installed.
Flask server deployed on a cloud platform (e.g., Heroku, AWS).
Deployment Steps
Clone repository, install dependencies, and configure environment variables.
Start Flask server (python api_server.py).
Testing Procedures
Unit tests for API endpoints and language model integration.
User acceptance testing for voice recognition accuracy and order processing.
Maintenance and Updates
Regular updates to menu items and prices.
Monitoring for performance and scalability.
7. Conclusion
Summary
The voice-activated KFC order assistant provides a seamless ordering experience through voice commands, leveraging natural language processing technologies.
Future Enhancements
Implement user accounts and order history.
Expand menu customization options.
Enhance natural language understanding capabilities.


