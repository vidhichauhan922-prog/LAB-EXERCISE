#program : 1

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
    
#program : 2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("A is largest")
elif b > a and b > c:
    print("B is largest")
else:
    print("C is largest")
    
    
program : 3

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
elif num % 2 != 0:
    print("Odd number")
else:
    print("Invalid input")
    
    
#program : 4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Addition =", a + b)
elif op == "-":
    print("Subtraction =", a - b)
elif op == "*":
    print("Multiplication =", a * b)
elif op == "/":
    print("Division =", a / b)
else:
    print("Invalid operator")
    
    
#program : 5

month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number")
    
    
#program : 6


temp = float(input("Enter temperature: "))

if temp > 40:
    print("Very Hot Weather")
elif temp >= 25:
    print("Warm Weather")
elif temp >= 10:
    print("Cool Weather")
else:
    print("Very Cold Weather")
    
    
#program : 7

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for voting.")
elif age > 0 and age < 18:
    print("You are not eligible for voting.")
else:
    print("Invalid age entered.")