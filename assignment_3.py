from student_system import (
    DATA_FILE,
    load_data,
    save_data,
    add_student_menu,
    search_student_menu,
    edit_student_menu,
    remove_student_menu,
    print_student_list)

def main():
    students = load_data(DATA_FILE)
    print("Welcome to the Students Enrollment system")

    while True:
        print("What would you like to do today?")
        print("-Add a student? enter 1")
        print("-Search for student 2")
        print("-Edit student info? enter 3")
        print("-Remove a student? enter 4")
        print("-Print the student list? enter 5")
        print("-Save the data to a file? enter 6")

        choice = input().strip()

        if choice == "1":
            add_student_menu(students)
        elif choice == "2":
            search_student_menu(students)
        elif choice == "3":
            edit_student_menu(students)
        elif choice == "4":
            remove_student_menu(students)
        elif choice == "5":
            print_student_list(students)
        elif choice == "6":
            save_data(DATA_FILE, students)
        else:
            print("Invalid selection. Please try again.")

        cont = input("Continue (y/yes) or exit (n/no)? ").strip().lower()
        if cont in ("n", "no"):
            break


if __name__ == "__main__":
    main()