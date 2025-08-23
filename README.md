# Gemini Chatbot Web App

A futuristic chatbot powered by **Gemini API**, built with **Python Flask** for the backend and **HTML/CSS/JS** for the frontend. It features a neon-themed UI with dynamic chat animations and light/dark mode toggle.

---

## Features

- Real-time chat with Gemini AI.
- Neon-themed, animated chat UI.
- Dark/Light mode toggle.
- Dynamic chat bubble animations.
- Responsive design for desktop and mobile.

---

## Project Structure
gemini-chatbot/
│
├── app.py            # Flask backend server
├── ai.py             # AI integration logic with Gemini API
├── chatbot.py        # Optional: chatbot helper functions
├── templates/
│   └── index.html    # Frontend HTML
├── static/
│   ├── style.css     # Optional separate CSS
│   └── script.js     # Optional separate JS
├── .env              # Environment variables
├── requirements.txt  # Python dependencies
└── README.md

---

## Requirements

- Python 3.10+
- Flask
- `python-dotenv`
- Gemini API Key

---

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot

pip install -r requirements.txt

GOOGLE_API_KEY=your_gemini_api_key_here

python app.py

