def add(a, b):
    return a + b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"The sum of {num1} and {num2} is {add(num1, num2)}")



def greet(name="vidhi", age=19):
    print(f"Hello {name}, you are {age} years old.")
    
greet(name="Alice", age=22)  
greet(name="janki")  
greet()  



def display_student_info(name, age, grade, school="XYZ School"):
    print(f"Name: {name}, Age: {age}, Grade: {grade}, School: {school}")

display_student_info(name="Sarah", age=16, grade="10th")
display_student_info(name="Tom", age=17, grade="11th", school="ABC High School")



def format_sentence(subject, verb, object):
    return f"{subject} {verb} {object}"

formatted_sentence = format_sentence(subject="The cat", verb="chases", object="the mouse")
print(formatted_sentence)



def rectangle_area(length, width):
    return length * width

area = rectangle_area(length=5, width=10)
print(f"Rectangle Area: {area}")



def power(base, exponent):
    return base ** exponent

result = power(base=2, exponent=3)
print(f"2 raised to the power of 3 is {result}")



def age_group(age):
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    else:
        return "Adult"

print(age_group(age=25))
print(age_group(age=10))



def area_of_circle(radius, pi=3.1416):
    return pi * (radius ** 2)

print(f"Area of circle: {area_of_circle(radius=5)}") 
print(f"Area of circle with custom pi: {area_of_circle(radius=5, pi=3.14)}")



def calculator(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return "Invalid operation"

print(f"Addition: {calculator(a=200, b=34, operation='add')}")
print(f"Subtraction: {calculator(a=100, b=20, operation='subtract')}")