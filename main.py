from datetime import datetime
from student import Student
from storage import load_students, save_students
from reports import student_report, class_report, save_text_report
from results import get_position_text

SUBJECTS = ["English Language", "Mathematics", "Biology", "Chemistry", "Physics"]


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def find_student(students, student_id):
    for student in students:
        if student.student_id.lower() == student_id.lower():
            return student
    return None


def register_student(students):
    print("\n--- REGISTER A NEW STUDENT ---")
    student_id = get_non_empty("Student ID: ")

    if find_student(students, student_id):
        print("A student with that ID already exists.")
        return

    full_name = get_non_empty("Full name: ")
    student_class = get_non_empty("Class/Form: ")
    gender = get_non_empty("Gender: ")

    while True:
        dob = get_non_empty("Date of birth (YYYY-MM-DD): ")
        try:
            datetime.strptime(dob, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date in YYYY-MM-DD format.")

    students.append(Student(student_id, full_name, student_class, gender, dob))
    save_students(students)
    print("Student registered successfully.")


def display_students(students):
    print("\n--- REGISTERED STUDENTS ---")
    if not students:
        print("No students have been registered.")
        return

    print(f"{'ID':<12} {'FULL NAME':<28} {'CLASS':<15} {'GENDER':<10}")
    print("-" * 68)
    for student in students:
        print(f"{student.student_id:<12} {student.full_name[:27]:<28} "
              f"{student.student_class[:14]:<15} {student.gender:<10}")


def search_student(students):
    search_text = get_non_empty("Enter student ID or name: ").lower()
    matches = [
        student for student in students
        if search_text in student.student_id.lower()
        or search_text in student.full_name.lower()
    ]

    if not matches:
        print("No matching student was found.")
        return

    for student in matches:
        print(student_report(student))


def update_student(students):
    student_id = get_non_empty("Enter the ID of the student to update: ")
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    new_name = input(f"Full name [{student.full_name}]: ").strip()
    new_class = input(f"Class/Form [{student.student_class}]: ").strip()
    new_gender = input(f"Gender [{student.gender}]: ").strip()
    new_dob = input(f"Date of birth [{student.date_of_birth}]: ").strip()

    if new_dob:
        try:
            datetime.strptime(new_dob, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. No changes were saved.")
            return

    if new_name:
        student.full_name = new_name
    if new_class:
        student.student_class = new_class
    if new_gender:
        student.gender = new_gender
    if new_dob:
        student.date_of_birth = new_dob

    save_students(students)
    print("Student information updated.")


def delete_student(students):
    student_id = get_non_empty("Enter the ID of the student to delete: ")
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    confirm = input(f"Delete {student.full_name}? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student record deleted.")
    else:
        print("Delete cancelled.")


def record_scores(students):
    student_id = get_non_empty("Enter student ID: ")
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("\nEnter scores from 0 to 100. Existing scores will be updated.")
    for subject in SUBJECTS:
        while True:
            current = student.scores.get(subject)
            prompt = f"{subject} score"
            if current is not None:
                prompt += f" (current: {current:g})"
            prompt += ": "

            try:
                score = float(input(prompt))
                if 0 <= score <= 100:
                    student.add_or_update_score(subject, score)
                    break
                print("Score must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    save_students(students)
    print("Scores saved successfully.")


def update_one_score(students):
    student_id = get_non_empty("Enter student ID: ")
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("Subjects:", ", ".join(SUBJECTS))
    subject = get_non_empty("Enter subject name exactly as shown: ")
    if subject not in SUBJECTS:
        print("That subject is not in the subject list.")
        return

    while True:
        try:
            score = float(input("Enter new score (0-100): "))
            if 0 <= score <= 100:
                student.add_or_update_score(subject, score)
                save_students(students)
                print("Score updated.")
                return
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def show_report_card(students):
    student_id = get_non_empty("Enter student ID: ")
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    report = student_report(student)
    print("\n" + report)
    save_choice = input("Save this report to a text file? (y/n): ").strip().lower()
    if save_choice == "y":
        safe_id = "".join(character for character in student.student_id
                          if character.isalnum() or character in "-_")
        path = save_text_report(report, f"report_{safe_id}.txt")
        print("Report saved to:", path)


def show_class_report(students):
    report = class_report(students)
    print("\n" + report)
    save_choice = input("Save class report to a text file? (y/n): ").strip().lower()
    if save_choice == "y":
        path = save_text_report(report, "class_result_summary.txt")
        print("Report saved to:", path)


def sort_students(students):
    if not students:
        print("No students to sort.")
        return

    print("1. Sort by average (highest to lowest)")
    print("2. Sort by name (A-Z)")
    choice = input("Choose: ").strip()

    if choice == "1":
        ordered = sorted(students, key=lambda item: item.average_score(), reverse=True)
    elif choice == "2":
        ordered = sorted(students, key=lambda item: item.full_name.lower())
    else:
        print("Invalid choice.")
        return

    print("\n--- SORTED STUDENTS ---")
    for position, student in enumerate(ordered, start=1):
        grade = student.grade() if student.scores else "N/A"
        print(f"{get_position_text(position)}  {student.full_name} | "
              f"Average: {student.average_score():.2f} | Grade: {grade}")


def show_menu():
    print("""
====================================================
       STUDENT RESULT MANAGEMENT SYSTEM
====================================================
1.  Register a new student
2.  View all students
3.  Search for a student
4.  Update student information
5.  Delete a student
6.  Record scores for five subjects
7.  Update one subject score
8.  View an individual report card
9.  View class results and statistics
10. Sort students
0.  Exit
====================================================""")


def main():
    students = load_students()
    print("Student Result Management System")
    print(f"{len(students)} student record(s) loaded.")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                register_student(students)
            elif choice == "2":
                display_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                record_scores(students)
            elif choice == "7":
                update_one_score(students)
            elif choice == "8":
                show_report_card(students)
            elif choice == "9":
                show_class_report(students)
            elif choice == "10":
                sort_students(students)
            elif choice == "0":
                save_students(students)
                print("Your records have been saved. Goodbye!")
                break
            else:
                print("Invalid option. Choose a number from the menu.")
        except (OSError, ValueError) as error:
            print("Something went wrong:", error)


if __name__ == "__main__":
    main()
