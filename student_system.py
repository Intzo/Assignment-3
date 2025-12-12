# -----------------------------
# Student class (OOP Section)
# -----------------------------

class Student:
    def __init__(self, student_id, first_name, last_name, gpa, semester):
        self.student_id = int(student_id)
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = float(gpa)
        self.semester = int(semester)

    def __str__(self):
        return f"{self.student_id}\t{self.first_name}\t{self.last_name}\t{self.gpa:.1f}\t{self.semester}"


# ----------------------------------
# Helper functions
# ----------------------------------

def find_student_by_id(students, student_id):
    for student in students:
        if student.student_id == int(student_id):
            return student
    return None


def find_student_by_name(students, first_name, last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    for student in students:
        if student.first_name.lower() == first_name and student.last_name.lower() == last_name:
            return student
    return None


def student_exists_by_name(students, first_name, last_name):
    return find_student_by_name(students, first_name, last_name) is not None


# ----------------------------------
# Persistence functions (File I/O)
# ----------------------------------

DATA_FILE = "data.txt"


def load_data(filename):
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 5:
                    continue
                try:
                    student = Student(*parts)
                    students.append(student)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass

    return students


def save_data(filename, students):
    with open(filename, "w", encoding="utf-8") as f:
        for student in students:
            f.write(f"{student.student_id},{student.first_name},{student.last_name},{student.gpa},{student.semester}\n")
    print("Data saved to local file successfully!")


# ----------------------------------
# Menu option functions
# ----------------------------------

def add_student_menu(students):
    while True:
        print("Enter id of the student, followed by the student's information.")
        student_id = input("Id: ").strip()
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        gpa = input("GPA: ").strip()
        semester = input("Semester: ").strip()

        if find_student_by_id(students, student_id):
            print("Incorrect Id. Id already exist in the system.")
        else:
            if student_exists_by_name(students, first_name, last_name):
                print("The student already enrolled. No action is required..")
            else:
                try:
                    new_student = Student(student_id, first_name, last_name, gpa, semester)
                    students.append(new_student)
                    print("Student Enrolled in the system")
                    print(new_student)
                except ValueError:
                    print("Invalid input. Please make sure Id, GPA, and Semester are valid numbers.")

        if input("Do you want to add more students? y(yes)/n(no) ").strip().lower() not in ("y", "yes"):
            break


def search_student_menu(students):
    while True:
        print("To search using the Id enter 1. To search using the first name and last name enter 2. Enter -1 to return.")
        choice = input().strip()

        if choice == "-1":
            break
        elif choice == "1":
            student = find_student_by_id(students, input("Please Enter the id: ").strip())
            print("Student found  " + str(student) if student else "Student not found")
        elif choice == "2":
            first = input("Please Enter the first name: ").strip()
            last = input("Please Enter the last name: ").strip()
            student = find_student_by_name(students, first, last)
            print("Student found  " + str(student) if student else "Student not found")
        else:
            print("Invalid selection. Please try again.")


def edit_student_menu(students):
    while True:
        user_input = input("Enter the id (-1 to return): ").strip()
        if user_input == "-1":
            break

        student = find_student_by_id(students, user_input)
        if student is None:
            print("Student not found")
        else:
            new_first = input("First name: ").strip()
            new_last = input("Last name: ").strip()
            new_gpa = input("GPA: ").strip()
            new_sem = input("Semester: ").strip()

            try:
                student.first_name = new_first
                student.last_name = new_last
                student.gpa = float(new_gpa)
                student.semester = int(new_sem)
                print("Student's new info is  " + str(student))
            except ValueError:
                print("Invalid input. No changes were made.")


def remove_student_menu(students):
    while True:
        student = find_student_by_id(students, input("Enter id: ").strip())
        if student:
            students.remove(student)
            print("Student removed")
        else:
            print("Student not found")

        if input("Remove more students? y/n ").strip().lower() not in ("y", "yes"):
            break


def print_student_list(students):
    if not students:
        print("No students enrolled yet.")
        return

    for student in sorted(students, key=lambda s: s.student_id):
        print(student)