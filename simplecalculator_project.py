#imports 
import re
import math 
#variables 
i = 0 
#def addition():

#def subtraction():
    
#def multiplication():
    
#def division():
while i == 0:
    print("\nThis is a simple calculator")
    print('please select operation from the list provided')
        #select operation
    print ("\n1: addition")
    print ("2: subtraction")
    print ("3: multiplication")
    print ("4: division")
    option = input("\nchoose your option: ")
    #if statements for each operation 

    if option == "1":
        print("addition")
        number1 = int(input("enter first number: "))
        number2 = int(input("enter second number: "))
        answer = number1 + number2
        i = 1
    elif option == "2":
        print('subtraction')
        number1 = int(input("enter first number: "))
        number2 = int(input("enter second number: "))
        answer = number1 - number2
        i = 1
    elif option == "3":
        print('multiplication')
        number1 = int(input("enter first number: "))
        number2 = int(input("enter second number: "))
        answer = number1 * number2
        i = 1
    elif option == "4":
        print('division')
        number1 = int(input("enter first number: "))
        number2 = int(input("enter second number: "))
        answer = number1 / number2
        i = 1
    else:
        print("invalid option")
        
print('The answer to the equation is',answer)