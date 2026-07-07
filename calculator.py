class calculator:
      
    def __init__(self):
         self.a=float(input("enter your first number"))
         self.b=float(input("enter your first number"))      
    def addition(self):
        sum= self.a + self.b
        print("additon=",sum)
    def substraction(self):
        sub= self.a-self.b
        print("substraction=",sub)
    def multiplication(self):
        multiply=self.a*self.b
        print("multiply=",multiply)
    def division(self):
        divide=self.a/self.b
        print("Division=",divide)
obj1=calculator() 
obj1.addition()
obj1.substraction()
obj1.multiplication()
obj1.division()
