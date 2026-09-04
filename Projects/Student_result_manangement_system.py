students = []


def add_student():
    name = input("\nEnter student name: ")

    marks = []

    subjects = ["Python", "DSA", "DBMS", "Maths", "AI"]

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks in {subject}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("❌ Marks must be between 0 and 100.")

            except ValueError:
                print("❌ Enter a valid number.")

    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("\n✅ Student added successfully!")


def show_students():
    if not students:
        print("\n❌ No students found.")
        return

    print("\n========== STUDENT RESULTS ==========")

    for student in students:
        print(f"""
Name       : {student['name']}
Marks      : {student['marks']}
Total      : {student['total']}/500
Percentage : {student['percentage']:.2f}%
Grade      : {student['grade']}
----------------------------------------
""")


def search_student():
    name = input("\nEnter student name: ").lower()

    for student in students:
        if student["name"].lower() == name:
            print("\n========== STUDENT FOUND ==========")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print(f"Percentage: {student['percentage']:.2f}%")
            print("Grade:", student["grade"])
            return

    print("❌ Student not found.")


def find_topper():
    if not students:
        print("\n❌ No students available.")
        return

    topper = max(students, key=lambda student: student["percentage"])

    print("\n========== TOPPER ==========")
    print("🏆 Name:", topper["name"])
    print(f"Percentage: {topper['percentage']:.2f}%")
    print("Grade:", topper["grade"])


def main():
    while True:

        print("\n==============================")
        print("   🎓 STUDENT RESULT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Find Topper")
        print("5. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            find_topper()

        elif choice == "5":
            print("\n👋 Program closed.")
            break

        else:
            print("❌ Invalid choice.")


main()
