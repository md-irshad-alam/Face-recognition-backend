import database

print("--- Checking Students Table ---")
students = database.get_all_students()
if students:
    for s in students:
        print(f"Found student: {s['id']} - {s['name']}")
else:
    print("No students found in the database.")

print("\n--- Checking Specific ID 1002 ---")
student = database.get_student_by_id('1002')
if student:
    print(f"Student 1002 found: {student}")
else:
    print("Student 1002 NOT found.")
