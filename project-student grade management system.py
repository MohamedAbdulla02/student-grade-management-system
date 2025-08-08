import csv
import os

students = []

def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B+'
    elif avg >= 60:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    try:
        marks1 = float(input("Enter marks for subject 1: "))
        marks2 = float(input("Enter marks for subject 2: "))
        marks3 = float(input("Enter marks for subject 3: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return
    
    total = marks1 + marks2 + marks3
    avg = total / 3
    grade = calculate_grade(avg)
    
    student = {
        'name': name,
        'roll': roll,
        'marks1': marks1,
        'marks2': marks2,
        'marks3': marks3,
        'total': total,
        'average': avg,
        'grade': grade
    }
    
    students.append(student)
    print(f"Student {name} added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("{:<10} {:<10} {:<7} {:<7} {:<7} {:<8} {:<8} {:<6}".format(
        "Roll", "Name", "M1", "M2", "M3", "Total", "Average", "Grade"
    ))
    for s in students:
        print("{:<10} {:<10} {:<7} {:<7} {:<7} {:<8} {:<8.2f} {:<6}".format(
            s['roll'], s['name'], s['marks1'], s['marks2'], s['marks3'],
            s['total'], s['average'], s['grade']
        ))
    print()

def search_student():
    roll = input("Enter roll number to search: ")
    found = False
    for s in students:
        if s['roll'] == roll:
            print("Student Found:")
            print(s)
            found = True
            break
    if not found:
        print("Student not found.\n")

def sort_students():
    sorted_list = sorted(students, key=lambda x: x['total'], reverse=True)
    print("Students sorted by total marks:")
    for s in sorted_list:
        print(f"{s['roll']} - {s['name']} - Total: {s['total']} - Grade: {s['grade']}")
    print()

def save_to_file():
    with open("students.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
    print("Records saved to students.csv\n")

def load_from_file():
    if os.path.exists("students.csv"):
        with open("students.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['marks1'] = float(row['marks1'])
                row['marks2'] = float(row['marks2'])
                row['marks3'] = float(row['marks3'])
                row['total'] = float(row['total'])
                row['average'] = float(row['average'])
                students.append(row)
        print("Loaded existing records from students.csv\n")

def main():
    load_from_file()
    while True:
        print("=== Student Grade Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Sort Students by Total Marks")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            sort_students()
        elif choice == '5':
            if students:
                save_to_file()
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
