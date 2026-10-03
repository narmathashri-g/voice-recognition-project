# Voice Assistant using Python

A voice-controlled assistant built with Python that listens to your commands through a microphone, understands them using speech recognition, and replies with voice.

## Features

- Voice command recognition
- Text-to-speech response
- Open YouTube
- Google search
- Tell time and date
- Save notes by voice
- Exit by voice command

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| SpeechRecognition | Speech-to-text |
| PyAudio | Microphone input |
| pyttsx3 | Text-to-speech |
| webbrowser | Opening websites |

## How It Works

Voice Input → Speech Recognition → Command Processing → Task Execution → Voice Response

## Requirements

- Python 3.8 or above
- Working microphone
- Internet connection (for Google Speech Recognition)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/voice-recognition-project.git
   cd voice-recognition-project
   ```
2. Install the libraries:
   ```
   pip install -r requirements.txt
   ```
3. Run the project:
   ```
   python voice_assistant.py
   ```

## Example Commands

- "Open YouTube"
- "What is the time"
- "Search Python tutorials"
- "Take a note"
- "Exit"

## Project Structure

```text
voice-recognition-project/
├── voice_assistant.py
├── requirements.txt
└── README.md
```

## Future Improvements

- Tamil language support
- Offline recognition using Vosk
- GUI interface

## Author

Narmathashri G

