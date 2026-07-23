#count=1   #iterator
#while count<=5:         #iteration #initialization 
#    print("hi")
#    count+=1

#Q1  1to100
# i=1
# while i<=100:           #stopping condition
#     print(i)
#     i+=1


# #Q2 100to1
# i=100  
# while i>=1:
#     print(i)
#     i-=1  

#Q3 table
# i=1
# a=int(input("enter the number for table"))
# while i<=10:
#     print(a*i)
#     i+=1

# #Q4         #traverse= ek ek element per jaana 
# nums =[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i < len(nums):
#     print(nums[i])
#     i+=1


# #Q5 
# nums =[1,4,9,16,25,36,49,64,81,100]
# x=16
# i=0
# while i < len(nums):
#     if (nums[i]==x):
#         print("Found at index",i)
#         break
#     else:
#         print("finding")    
#     i+=1

#continue
# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# nums =[1,4,9,16,25,36,49,64,81,100]
# for i in (nums):
#     print(i)

nums =(1,4,9,16,25,36,49,64,81,100,36)
x=36
a=0
for i in nums:
    if (i==36):
     print("number is found at",a)
    a+=1
