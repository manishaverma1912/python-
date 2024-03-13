num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the Second  number : "))
print("which option you want to choose =\n1.Addition \n2.Subtraction\n3.Multiplication\n4.division ")
option = int(input("enter the option: "))
if option == 1:
    print(" The addition of num1 and num2 is : ", (num1+num2))
elif option == 2:
    print(" The  subtraction of  num1 and num2 is :", (num1-num2))
elif option == 3:
    print("The Multiplication of num1 and num2  is :", (num1*num2))
elif option == 4:
    print("The division  of num1 and num2 is :", (num1/num2))

else:
    print(" It is  an invalid option ")








