print("   🙏🏻Welcome🙏🏻\nName:Prithvi saini\nDate:30-10-2025\nProject:Daily Calorie Tracker CLI\nThis tool detect your daliy calorie\n ")

meal=[]
calorie=[]
user=int(input("\nYour total colorie per day="))
x=int(input("Enter number of your today meals"))
for i in range(x):
    m=input("\nEnter your meal name:")
    c=int(input("Enter  number of calorie for this food:"))
    meal.append(m)  
    calorie.append(c)
    
print(meal)
print(calorie)

s=sum(calorie)
print(f"\nThe  total calories you eat today {s}")
a=s/x
print("\nYour today average calorie =",a)

for i in range(x):
    print(f"{meal[i]}\t\t{calorie[i]}")
print("--------------------------------")
print(f"Total:\t\t{s}")
print(f"Average:\t{a:.2f}")



if user<s:
         print("\n🚨warning your today calories is higher then per day calories")
elif user==s:
         print("\n⚠️  You are very near to cross your daily limit")
else:
         print("🕺Great! You are within your daily calorie limit.")

         
