print("   🙏🏻Welcome🙏🏻\nName:Prithvi saini\nDate:15-11-2025\nProject:GradeBook Analyzer\nAssignment Title: Analyzing and Reporting Student Grades\n ")
def number():
    marks={}
    x=int(input("Enter how many students are in the class."))
    for i in range(x):
        s=input("\nEnter name of students")
        m=int(input("Enter marks of students"))
        marks[s]=m
    print(marks)

    total_sum=sum(marks.values())
    avg=total_sum/x
    print("Average number is:",avg)

    import statistics 
    lt=list(marks.values())
    median=statistics.median(lt)
    print("Median number is:",median)

    maxx=max(lt)
    print("Maximum ",maxx)

    minn=min(lt)
    print("Minimum value is:",minn)

    student_grade={}
    for s,st in marks.items():
        if st >=90 and st<=100:
            student_grade[s]="A"
        elif st>=80 and st<=89:
            student_grade[s]="B"
        elif st>=70 and st<=79:
            student_grade[s]="C"
        elif st>=60 and st<=69:
            student_grade[s]="D"
        else:
            student_grade[s]="f"
            
    print("student get grade:",student_grade)
    
number()
    
    
    
