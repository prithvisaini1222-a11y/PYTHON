class student:
    college_name="k.r. mangalam"
    def __init__(self,rollno,name,mark1,mark2,mark3):
        self.rollno=rollno
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def display(self):
         print("Roll No:",self.rollno)
         print("Name:",self.name)
         print("Mark1:",self.mark1)
         print("Mark2:",self.mark2)
         print("Mark3:",self.mark3)
         
    def average(self):
         Total_marks=self.mark1+self.mark2+self.mark3
         avg_marks=Total_marks/3
         print(avg_marks)
        
obj1=student(18,"Prithvi",99,95,98)
obj1.display()
obj1.average()
