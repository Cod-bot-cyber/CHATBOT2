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

📊 Project Completion Status – Course Enrollment Advisor Chatbot
	1.	Database Setup (Students, Courses, Enrollments, QA) → ✅ 100% complete
	•	Students table
	•	Courses with prerequisites + seats
	•	Enrollments mapping
	2.	Backend Logic (Flask + Python) → ✅ ~90% complete
	•	Roll number detection
	•	Student details fetch
	•	View enrolled courses
	•	Suggest courses
	•	Enroll in course (with prerequisite + seat check)
	•	FAQ fallback
	•	Session reset support
(improvement possible: better NLP understanding, error handling, course recommendation logic)
	3.	Frontend (index.html) → ✅ ~80% complete
	•	Chatbox UI with animation and styling
	•	Bot + User messages display
	•	Dynamic buttons (View Courses, Suggest Courses, Enroll)
	•	Basic interactivity working
	•	Black theme + custom styling
    •   pleasing background 
(improvement possible: modern UI components, typing indicator, better button styles, mobile responsive design)
	4.	User Experience (UX) → ✅ ~70% complete
	•	Roll number based conversation working
	•	Menu-driven quick replies
	•	Basic course advising flow done
    •   toggle dark mode / light mode
	•   manipulate predefined data
(improvement possible: proactive suggestions, smarter FAQ, better error messages, voice support, analytics)

⸻

🎯 Overall Completion: ~80% ready
