students = [
    ("Riya", 88),
    ("Aman", 95),
    ("Sara", 72),
    ("Rahul", 90),
    ("Priya", 85)
]

students.sort(key=lambda student: student[1], reverse=True)

print(students)
