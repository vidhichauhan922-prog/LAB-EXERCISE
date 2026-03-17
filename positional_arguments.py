
def add(a,b):
    print("a",a)
    print("b",b)
    return a+b
result=add(2,5)
print("result:",result)



def greet(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")

greet("Alice", "morning")
greet("morning", "Alice")



def subtract(a, b):
    result = a - b
    print(f"The result of {a} - {b} is: {result}")

subtract(10, 3) 
subtract(3, 10) 



def student_info(name,roll,marks):
    print("name:",name)
    print("roll no:",roll)
    print("marks:",marks)

student_info("ravi",101,85)


def calculate_bmi(weight, height):
    # BMI = weight / (height * height)
    bmi = weight / (height ** 2)
    print(f"With a weight of {weight}kg and height of {height}m...")
    print(f"Your BMI is: {round(bmi, 2)}")

calculate_bmi(70, 1.75)



def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interest :",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)



def ar_circle(r):
    ar_circle=3.14*r*r
    print("area of circle:",ar_circle)
ar_circle(1.5)
ar_circle(4)



def check_number(n):
    
    if n > 0:
        print(f"The number {n} is POSITIVE.")
    elif n < 0:
        print(f"The number {n} is NEGATIVE.")
    else:
        print(f"The number is ZERO.")

check_number(10)   # Positive
check_number(-5)   # Negative
check_number(0)    # Zero



def check_odd_even(number):

    if number % 2 == 0:
        print(f"{number} is an EVEN number.")
    else:
        print(f"{number} is an ODD number.")

check_odd_even(42)  # Even
check_odd_even(17)  # Odd
check_odd_even(0)   # Even (Zero is technically even!)



def subtract_numbers(a, b):
    result = a - b
    print(f"Subtraction: {a} - {b} = {result}")

# Position 1 is 'a', Position 2 is 'b'
subtract_numbers(50, 20)  # Output: 30



def multiply_numbers(x, y):
    result = x * y
    print(f"Multiplication: {x} * {y} = {result}")

multiply_numbers(12, 4)  # Output: 48



def divide_numbers(dividend, divisor):
    if divisor == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = dividend / divisor
        print(f"Division: {dividend} / {divisor} = {result}")


divide_numbers(100, 5)  # Output: 20.0
