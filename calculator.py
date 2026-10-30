print("===============MATHS CALCULATOR===============")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Square Root")
print("7. Power")
print("8. Percentage")
print ("9. Exit")
print ("============================")

choice=int(input("Enter your choice : "))

if choice==9:
    print ("THANK YOU")
elif choice==1:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("Answer: ",a+b)
elif choice==2:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("Answer: ",a-b)
elif choice==3:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("Answer: ",a*b)
elif choice==4:
    a=float(input("Enter the dividend: "))
    b=float(input("Enter the divisor: "))
    print("Answer: ",a/b)
elif choice==5:
    a=float(input("Enter a number: "))
    print("Answer: ",a**2)
elif choice==6:
    a=float(input("Enter a number: "))
    print("Answer: ",a**0.5)
elif choice==7:
    a=float(input("Enter the number: "))
    b=float(input("Enter the power: "))
    print("Answer: ",a**b)
elif choice==8:
    a=float(input("Enter total value: "))
    b=float(input("Enter the desired value: "))
    print("Answer: ",(a*b)/100)
else:
    print("Invalid choice")
