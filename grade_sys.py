### print("🙏🏻 Welcome 🙏🏻\nName: Prithvi Saini\nDate: 15-11-2025\nProject: GradeBook Analyzer\nAssignment Title: Analyzing and Reporting Student Grades\n")

import statistics

def analyze_class():
    marks = {}
    x = int(input("Enter how many students are in the class: "))

    for i in range(x):
        s = input("\nEnter name of student: ")
        m = int(input("Enter marks of student: "))
        marks[s] = m

    print("\nStudent Marks:", marks)


    total_sum = sum(marks.values())
    avg = total_sum / x
    print("Average marks:", avg)


    lt = list(marks.values())
    median = statistics.median(lt)
    print("Median:", median)

    # Max & Min
    print("Maximum marks:", max(lt))
    print("Minimum marks:", min(lt))

    student_grade = {}
    for s, st in marks.items():
        if 90 <= st <= 100:
            student_grade[s] = "A"
        elif 80 <= st <= 89:
            student_grade[s] = "B"
        elif 70 <= st <= 79:
            student_grade[s] = "C"
        elif 60 <= st <= 69:
            student_grade[s] = "D"
        else:
            student_grade[s] = "F"
    print("\nGrades:", student_grade)

  
    passed_students = [name for name, m in marks.items() if m >= 40]
    failed_students = [name for name, m in marks.items() if m < 40]
    print("\nPassed:", passed_students, " | Count:", len(passed_students))
    print("Failed:", failed_students, " | Count:", len(failed_students))

    return marks, student_grade


def print_results_table(marks, student_grade):
    print("\n--------------------------------------")
    print("       RESULTS TABLE")
    print("--------------------------------------")
    print("Name\t\tMarks\tGrade")
    print("--------------------------------------")
    for student_name in marks:
        print(f"{student_name}\t\t{marks[student_name]}\t{student_grade[student_name]}")
    print("--------------------------------------")

while True:
    marks, student_grade = analyze_class()
    print_results_table(marks, student_grade)
    
    choice = input("Do you want to analyze another class? (y/n): ")
    if choice.lower() != 'y':
        print("\n Program Ended — Thank You!")
    
