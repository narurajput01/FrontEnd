print("Do you want to enter your information")
ans1=str(input("Enter your ans :"))
if (ans1=="yes"):
    name=str(input("Enter your name here:"))
    age=int(input("Enter your age here:"))
    admission_no=int(input("Enter your admission no here :"))
    
    print("Your name is",name,"and your age is",age,"and your admission no is",admission_no)
else:
    print("Thank you for visiting our website")