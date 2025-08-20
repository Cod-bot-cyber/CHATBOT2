# CHATBOT PROTOTYPE
A smart Course Enrollment Advisor Chatbot built with Flask and MySQL.   🎓 Helps students check their details, view enrolled courses, get personalized course suggestions, and enroll in new courses interactively.   💬 Includes a modern chat interface with buttons, emojis, and session memory.   🚀 Built for a Hackathon by Team Bot Busters.

# 🎓 Course Enrollment Advisor Chatbot

A smart and interactive chatbot that helps students view, suggest, and enroll in courses using their roll number.  
Built using **Python (Flask)**, **MySQL**, and a modern **chat-based UI**.

---

## 🚀 Features
- 🤖 Chatbot interface for student queries  
- 📌 Student details lookup using roll number  
- 📚 View enrolled courses  
- 💡 Suggest courses based on availability / year  
- 📝 Enroll in a new course dynamically  
- 🖥️ Interactive frontend with chat UI + buttons  
- 🔄 Session reset option  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)  
- **Database:** MySQL  
- **Frontend:** HTML, CSS, JavaScript  
- **Libraries:**  
  - `mysql-connector-python` (for DB connection)  
  - `Flask` (for API + web server)  

---

## 📂 Project Structure
---
Chatbot-Project/
│── app.py                # Flask backend (API + routing)
│── chatbot.py            # Chatbot logic functions
│── data_preparation.py   # Database setup (tables, sample data)
│── db_config.py          # MySQL config (username, password, host)
│── templates/
│    └── index.html       # Chatbot frontend
│── static/
│    └── (optional) CSS/JS files or images
│── README.md             # Project documentation

🎮 How to Use
	1.	Open the chatbot in your browser.
	2.	Enter your Roll Number (e.g., 102).
	3.	Chatbot will show your details and give menu options:
	•	View Courses → See enrolled courses
	•	Suggest Courses → Get course
