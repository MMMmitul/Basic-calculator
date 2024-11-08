print("Welcome to Calculator project")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

option=int(input("Select an option for basic calculator operation: "))

if option==1:
    number1= int(input("please Enter your first number: "))
    number2 =int(input("please Enter your second number: "))
    number3= "Addition is: "+str(number1+ number2)
    print(number3)


elif option==2:
    number1= int(input("please Enter your first number: "))
    number2 =int(input("please Enter your second number: "))
    number3= "Subtraction is: "+str(number1-number2)
    print(number3)


elif option==3:
    number1= int(input("please Enter your first number: "))
    number2 =int(input("please Enter your second number: "))
    number3= "Multiplication is: "+str(number1*number2)
    print(number3)

elif option==4:
    number1= int(input("please Enter your first number: "))
    number2 =int(input("please Enter your second number: "))
    number3= "Division is: "+str(number1/number2)
    print(number3)

else:
    print("You have choose an invalid operation. Please choose a valid one")
