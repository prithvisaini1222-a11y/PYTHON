# x=int(input("enter  1st number"))
# y=int(input("enter  2nd number"))
# print(x+y)


# x=int(input("enter side of square"))
# y= x*x
# print(y)

# x=float(input("enter 1st number"))
# y=float(input("enter 2nd number"))
# print((x+y)/2)


def add_employee():
    try:
        with open("emp.txt","a") as f:
            id = input("ID:")
            name = input("Name:")
            salary = input("Salary:")
            f.write(f"{id},{name},{salary}\n")
    except ValueError:
        print("Value Error")

def display():
    try:
        with open("emp.txt","r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")

def search(emp_id):
    try:
        with open("emp.txt","r") as f:
            for line in f:
                if emp_id in line:
                    print(line)
    except FileNotFoundError:
        print("File not found")
