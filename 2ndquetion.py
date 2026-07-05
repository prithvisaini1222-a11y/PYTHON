 #write a program to read student marks from text file and dispaly highest and average marks.also use exception handling
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

def read_student_marks(file_name):
    students = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    data = line.strip().split(',')
                    name = data[0]
                    marks = float(data[1])
                    students.append(Student(name, marks))
                except ValueError:
                    print(f"Skipping invalid entry: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")
    return students

def calculate_highest_and_average(students):
    if not students:
        print("No student data available.")
        return None, None
    highest = max(students, key=lambda x: x.marks)
    avg = sum(student.marks for student in students) / len(students)
    return highest, avg

def display_results(highest, avg):
    if highest and avg is not None:
        print(f"Highest Marks: {highest.marks} by {highest.name}")
        print(f"Average Marks: {avg:.2f}")

if __name__ == "__main__":
    students = read_student_marks('student_marks.txt')
    highest, avg = calculate_highest_and_average(students)
    display_results(highest, avg)


#create menu driven calculate  with expection handling for invalid oeration and zero devision
