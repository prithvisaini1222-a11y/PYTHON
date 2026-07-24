class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name of student",self.name)
        print("Age of student",self.age)
class student(person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print("Roll no of student",self.rollno)
        print("Marks of students",self.marks)
class employee(person):
    def __init__(self,name,age, basic_salary , hra,ba):
        super().__init__(name,age)
        self.basic_salary=basic_salary
        self.hra=hra
        self.ba=ba
        self.x= self.basic_salary + self.hra + self.ba

    def diplay(self):
        super().display()
       

    def addition(self):
        x=self.basic_salary + self.hra + self.ba
        print("Total salary",x )
        
        
        
obj1=student("kali",18,42,92)
obj1.display()
obj2=employee("Tannu", 18 , 550000,30000,20000)
obj2.display()
obj2.addition()
