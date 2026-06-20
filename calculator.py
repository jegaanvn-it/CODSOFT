import math
def add(n1,n2): 
    print("Result: ",n1+n2)
def subtract(n1,n2):
    print("Result: ",n1-n2)
def multiply(n1,n2):
    print("Result: ",n1*n2)
def divide(n1,n2):
    try:
        print("Result: ",n1/n2)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
def modulus(n1,n2):
    try:
        print("Result: ",n1%n2)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
def exponentiation(n1,n2):
    print("Result: ", n1**n2)
def floor_division(n1,n2):
    try:
        print("Result: ",n1//n2)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
def square_root(n1):
    if n1 < 0:
        print("Result: ",f"{math.sqrt(-n1)}i")
    else:
        print("Result: ",math.sqrt(n1))
def cube_root(n1):
    if n1 >= 0:
        print("Result: ", math.pow(n1, 1/3))
    else:
        print("Result: ", -math.pow(n1*-1, 1/3))
def logarithm(n1):
    try:
        print("Result: ",math.log(n1))
    except ValueError:
        print("Error: Logarithm is not defined for zero or negative numbers")
def sine(n1):
    print("Result: ",math.sin(n1*math.pi/180))
def cosine(n1):
    print("Result: ",math.cos(n1*math.pi/180))
def tangent(n1):
    print("Result: ", math.tan(math.radians(n1)))
def cotangent(n1):
    try:
        print("Result: ",1/math.tan(math.radians(n1)))
    except ZeroDivisionError:
        print("Cotangent undefined")

print("================================================")
print("Calculator")
print("================================================")
print("|1. Addition          |")
print("|2. Subtraction       |")
print("|3. Multiplication    |")
print("|4. Division          |")
print("|5. Modulus           |")
print("|6. Exponentiation    |")
print("|7. Floor Division    |")
print("|8. Square Root       |")
print("|9. Cube Root         |")
print("|10. Logarithm        |")
print("|11. Sine             |")
print("|12. Cosine           |")
print("|13. Tangent          |")
print("|14. Cotangent        |")
print("|15. Exit             |")
print("================================================")

while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Error: Invalid choice")
        continue
    print("================================================")
    if choice == 1:
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
        add(n1,n2)
    elif choice == 2:
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
        subtract(n1,n2)
    elif choice == 3:
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
        multiply(n1,n2)
    elif choice == 4:
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
        divide(n1,n2)
    elif choice == 5:
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
        modulus(n1,n2)
    elif choice == 6:
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
        exponentiation(n1,n2)
    elif choice == 7:
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
        floor_division(n1,n2)
    elif choice == 8:
        n1=float(input("Enter the number: "))
        square_root(n1)
    elif choice == 9:
        n1=float(input("Enter the number: "))
        cube_root(n1)
    elif choice == 10:
        n1=float(input("Enter the number: "))
        logarithm(n1)
    elif choice == 11:
        n1=float(input("Enter the number: "))
        sine(n1)
    elif choice == 12:
        n1=float(input("Enter the number: "))
        cosine(n1)
    elif choice == 13:
        n1=float(input("Enter the number: "))
        tangent(n1)
    elif choice == 14:
        n1=float(input("Enter the number: "))
        cotangent(n1)
    elif choice == 15:
        break
    else:
        print("Invalid choice")
    print("================================================")

print("Thank you for using the calculator")
print("================================================")
