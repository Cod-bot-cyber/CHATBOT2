import mysql.connector
from db_config import db_config

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS chatbot")
cursor.execute("USE chatbot")

cursor.execute("""
CREATE TABLE IF NOT EXISTS qa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(255),
    answer VARCHAR(255)
)
""")

qa_pairs = [
    ("hello", "Hi!"),
    ("how are you", "I am good, thank you!"),
    ("what is your name", "I am your Course Enrollment Advisor Chatbot."),
    ("bye", "Goodbye!"),
]

cursor.executemany(
    "INSERT IGNORE INTO qa (question, answer) VALUES (%s, %s)", qa_pairs
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_number INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    class VARCHAR(20),
    section VARCHAR(5)
)
""")

students_data = [
    (101, "Rahul", "Sharma", "10", "A"),
    (102, "Anjali", "Verma", "10", "B"),
    (103, "Aman", "Gupta", "11", "A"),
]

cursor.executemany("""
INSERT IGNORE INTO students (roll_number, first_name, last_name, class, section)
VALUES (%s, %s, %s, %s, %s)
""", students_data)

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    year INT,
    credits INT,
    prerequisites VARCHAR(200),
    seats_available INT
)
""")

courses_data = [
    ("Data Structures", 2, 4, "None", 3),
    ("Algorithms", 3, 4, "Data Structures", 2),
    ("Database Systems", 3, 3, "None", 5),
]

cursor.executemany("""
INSERT IGNORE INTO courses (name, year, credits, prerequisites, seats_available)
VALUES (%s, %s, %s, %s, %s)
""", courses_data)

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_courses (
    roll_number INT,
    course_id INT,
    FOREIGN KEY (roll_number) REFERENCES students(roll_number),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

enrollments = [
    (101, 1),  
    (102, 2),  
]

cursor.executemany("""
INSERT IGNORE INTO student_courses (roll_number, course_id) VALUES (%s, %s)
""", enrollments)

conn.commit()
cursor.close()
conn.close()

print("✅ Database setup completed with QA, Students, Courses, and Enrollments.")
