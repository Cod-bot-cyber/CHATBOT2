from flask import Flask, request, jsonify, render_template
from ai import smalltalk_answer
from chatbot import (
    get_answer,
    get_student_courses,
    enroll_in_course,
    get_student_info_by_keywords,
    suggest_courses
)

app = Flask(__name__)
user_states = {} 

@app.route("/")
def home():
    return render_template("index.html")

def extract_roll_from_text(text: str):
    for w in text.split():
        if w.isdigit():
            return int(w)
    return None

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = (data.get("question") or "").strip()
    q_lower = question.lower()

    roll_number = extract_roll_from_text(question)
    if roll_number:
        user_states["current_user"] = roll_number
        info = get_student_info_by_keywords(roll_number, question)
        return jsonify({
            "answer": f"🤖 Hi! Found Roll No {roll_number}.\n{info}\n",
        })

    if "current_user" in user_states:
        roll_number = user_states["current_user"]

        if q_lower in ["view courses", "1"]:
            return jsonify({"answer": get_student_courses(roll_number), "buttons": []})

        if q_lower in ["suggest courses", "2"]:
            return jsonify({"answer": suggest_courses(roll_number), "buttons": []})

        if q_lower.startswith("enroll") or q_lower in ["3"]:
            course_name = ""
            if "enroll" in q_lower:
                parts = question.split(" ", 1)
                if len(parts) > 1:
                    course_name = parts[1].strip()
            if not course_name:
                return jsonify({"answer": "✍️ Please type: Enroll <course name>", "buttons": []})
            return jsonify({"answer": enroll_in_course(roll_number, course_name), "buttons": []})

        if any(k in q_lower for k in ["first name","firstname","last name","lastname","class","section"]):
            return jsonify({"answer": get_student_info_by_keywords(roll_number, question), "buttons": []})

        if "reset" in q_lower:
            user_states.clear()
            return jsonify({"answer": "🔄 Session reset. Enter your roll number again.", "buttons": []})

    ans = get_answer(question)
    if not ans:  
        ans = smalltalk_answer(question)

    return jsonify({"answer": ans, "buttons": []})

if __name__ == "__main__":
    app.run(debug=True, port=5050)
