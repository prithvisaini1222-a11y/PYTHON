# define a class student with attributes( name,roll,marks) add methods to accept details display setails fond grade based on marks


#2nd


class Student:
    def __init__(self, name="", roll=0, marks=0):
        # Constructor to initialize student details
        self.name = name
        self.roll = roll
        self.marks = marks

    def accept_details(self):
        # Method to accept student details from the user
        self.name = input("Enter the student's name: ")
        self.roll = int(input("Enter the roll number: "))
        self.marks = float(input("Enter the marks: "))

    def display_details(self):
        # Method to display student details
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll}")
        print(f"Marks: {self.marks}")

    def find_grade(self):
        # Method to calculate grade based on marks
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

if __name__ == "__main__":
    student = Student()  # Create a new student object
    student.accept_details()  # Accept student details
    student.display_details()  # Display the details
    grade = student.find_grade()  # Find grade
    print(f"Grade: {grade}")
