from flask import Flask, request, jsonify, render_template
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

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question","").strip()
    q_lower = question.lower()

    words = question.split()
    roll_number = None
    for w in words:
        if w.isdigit():
            roll_number = int(w)
            break

    if roll_number:
        user_states["current_user"] = roll_number
        info = get_student_info_by_keywords(roll_number, question)
        return jsonify({
            "answer": f"🤖 Hi! Found Roll No {roll_number}.\n{info}\nChoose an option:",
            "buttons": ["View courses", "Suggest courses", "Enroll"]
        })

    if "current_user" in user_states:
        roll_number = user_states["current_user"]
        if question.lower() in ["view courses","1"]:
            answer = get_student_courses(roll_number)
        elif question.lower() in ["suggest courses","2"]:
            answer = suggest_courses(roll_number)
        elif question.lower().startswith("enroll") or question.lower() in ["3"]:
            if "enroll" in q_lower:
                parts = q_lower.split("enroll",1)
                course_name = parts[1].strip() if len(parts)>1 else ""
                if course_name:
                    answer = enroll_in_course(roll_number, course_name)
                else:
                    answer = "✍️ Please type: Enroll <course name>"
            else:
                answer = "✍️ Please type: Enroll <course name>"
        elif any(k in q_lower for k in ["first name","last name","lastname","class","section"]):
            answer = get_student_info_by_keywords(roll_number, question)
        elif "reset" in q_lower:
            user_states.clear()
            answer = "🔄 Session reset. Enter your roll number again."
        else:
            answer = get_answer(question)
        return jsonify({"answer": answer, "buttons":[]})

    if "suggest" in q_lower or "recommend" in q_lower or "courses" in q_lower:
        return jsonify({"answer": suggest_courses(), "buttons":[]})

    return jsonify({"answer": get_answer(question), "buttons":[]})

if __name__=="__main__":
    app.run(debug=True, port=5050)
