import mysql.connector
from db_config import db_config

conn = mysql.connector.connect(**db_config)

def get_answer(question):
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT question, answer FROM qa")
    results = cursor.fetchall()
    cursor.close()
    for q, a in results:
        if q.lower() in question.lower():
            return a
    return "🤖 I don't understand the question. You can type your roll number or ask me to suggest courses."

def get_student_courses(roll_number):
    cursor = conn.cursor(buffered=True)
    cursor.execute("""
        SELECT c.name 
        FROM courses c
        JOIN student_courses sc ON c.course_id = sc.course_id
        WHERE sc.roll_number=%s
    """, (roll_number,))
    results = cursor.fetchall()
    cursor.close()
    if results:
        courses = [r[0] for r in results]
        return f"📚 You are enrolled in: {', '.join(courses)}"
    return "📚 You are not enrolled in any courses yet."

def enroll_in_course(roll_number, course_name):
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT course_id, prerequisites, seats_available FROM courses WHERE name=%s", (course_name,))
    course = cursor.fetchone()
    if not course:
        cursor.close()
        return f"⚠️ Course {course_name} not found!"
    course_id, prereq, seats = course
    cursor.execute("SELECT * FROM student_courses WHERE roll_number=%s AND course_id=%s", (roll_number, course_id))
    if cursor.fetchone():
        cursor.close()
        return f"⚠️ You are already enrolled in {course_name}."
    if prereq.lower() != "none":
        cursor.execute("""
            SELECT c.name FROM courses c
            JOIN student_courses sc ON c.course_id = sc.course_id
            WHERE sc.roll_number=%s
        """, (roll_number,))
        enrolled_courses = [r[0].lower() for r in cursor.fetchall()]
        cursor.close()
        if prereq.lower() not in enrolled_courses:
            return f"⚠️ You need to complete {prereq} before enrolling in {course_name}."
    if seats <= 0:
        cursor.close()
        return f"⚠️ No seats left in {course_name}."
    cursor.execute("INSERT INTO student_courses (roll_number, course_id) VALUES (%s,%s)", (roll_number, course_id))
    cursor.execute("UPDATE courses SET seats_available=seats_available-1 WHERE course_id=%s", (course_id,))
    conn.commit()
    cursor.close()
    return f"✅ Successfully enrolled in {course_name}!"

def get_student_info_by_keywords(roll_number, query):
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT first_name, last_name, class, section FROM students WHERE roll_number=%s", (roll_number,))
    result = cursor.fetchone()
    cursor.close()
    if not result:
        return "⚠️ Student not found!"
    first_name, last_name, class_, section = result
    q_lower = query.lower()
    if "first name" in q_lower or "firstname" in q_lower:
        return first_name
    if "last name" in q_lower or "lastname" in q_lower:
        return last_name
    if "class" in q_lower:
        return class_
    if "section" in q_lower:
        return section
    return f"🎓 Roll No: {roll_number}, Name: {first_name} {last_name}, Class: {class_}, Section: {section}"

def suggest_courses(roll_number=None):
    cursor = conn.cursor(buffered=True)
    if roll_number:
        cursor.execute("SELECT class, first_name FROM students WHERE roll_number=%s", (roll_number,))
        student = cursor.fetchone()
        if not student:
            cursor.close()
            return "⚠️ Student not found!"
        student_class, first_name = student
    else:
        student_class, first_name = 0, None
    cursor.execute("SELECT name, year, prerequisites, seats_available FROM courses")
    courses = cursor.fetchall()
    cursor.close()
    enrolled_courses = []
    if roll_number:
        cursor = conn.cursor(buffered=True)
        cursor.execute("""
            SELECT c.name FROM courses c
            JOIN student_courses sc ON c.course_id = sc.course_id
            WHERE sc.roll_number=%s
        """, (roll_number,))
        enrolled_courses = [r[0].lower() for r in cursor.fetchall()]
        cursor.close()
    suggestions = []
    for name, year, prereq, seats in courses:
        if seats <= 0:
            continue
        if roll_number and prereq.lower() != "none" and prereq.lower() not in enrolled_courses:
            continue
        suggestions.append(f"{name} (Seats: {seats}) | Prerequisite: {prereq}")
    if suggestions:
        if first_name:
            return f"🤖 Hi {first_name}, I recommend:\n- " + "\n- ".join(suggestions)
        return "🤖 Available courses:\n- " + "\n- ".join(suggestions)
    return "⚠️ No eligible courses available right now."
