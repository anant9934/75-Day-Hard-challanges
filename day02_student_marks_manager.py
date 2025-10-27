"""
Student Marks Manager
A beginner Python project to manage marks using lists, tuples, dictionaries, and strings.

Features:
- Add a student
- Add or update marks for a student
- View all student records

Author: ANANT KUMAR
Date: 27-10-2025
"""

# This list stores all students' details
class_list = []

# Function to add a new student
def add_student(name, roll, dob):
    student = {
        "name": name,          # string
        "info": (roll, dob),   # tuple (roll number, date of birth)
        "marks": {}            # dictionary: subject as key, score as value
    }
    class_list.append(student)
    print(f"Added student: {name}")

# Function to add or update marks for an existing student
def add_mark(name, subject, score):
    for student in class_list:
        if student['name'].lower() == name.lower():
            student['marks'][subject] = score
            print(f"Marks updated for {name} in {subject}: {score}")
            return
    print("Student not found.")

# Function to display all students and their details
def view_students():
    if not class_list:
        print("No students yet.\n")
        return
    print("\n--- Student Records ---")
    for student in class_list:
        print(f"Name      : {student['name']}")
        print(f"Roll/DOB  : {student['info']}")
        print(f"Marks     : {student['marks']}\n")

# Main menu for interactive user experience
def menu():
    print("\n--- Student Marks Manager ---")
    print("1. Add a student")
    print("2. Add/Update student marks")
    print("3. View all students")
    print("4. Exit")

# Program entry point
if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose (1-4): ").strip()
        if choice == "1":
            name = input("Student Name: ")
            roll = input("Roll Number: ")
            dob = input("Date of Birth (dd-mm-yyyy): ")
            add_student(name, roll, dob)
        elif choice == "2":
            name = input("Student Name: ")
            subject = input("Subject: ")
            score = input("Score: ")
            # Optional: convert score to int if you want only numbers
            try:
                score = int(score)
            except ValueError:
                print("Please enter a valid number for score.")
                continue
            add_mark(name, subject, score)
        elif choice == "3":
            view_students()
        elif choice == "4":
            print("Goodbye! Work saved.")
            break
        else:
            print("Invalid choice. Try again.")
