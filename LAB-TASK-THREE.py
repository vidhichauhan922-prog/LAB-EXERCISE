P = float(input("Principal amount (P) daalein: "))
R = float(input("Rate of interest (R) daalein (% per year): "))
T = float(input("Time (T) daalein (years): "))
SI = (P * R * T) / 100
print("Simple Interest =", SI)


num1 = float(input("enter the number: "))
num2 = float(input("enter the number: "))
if num1 > num2:
    maximum = num1
else:
    maximum = num2
print("Maximum number =", maximum)


i = 1
while i <= 5:
    print(i)
    i += 1
    
for i in range(1, 6):
    print(i)
    
    
my_string = "Hello, World!"
length = len(my_string)
print("String ki length =", length)


print("Welcome to Python Programming!")

my_string = input("Apni string daalein: ")
if my_string:
    first_char = my_string[0] 
    print("String ka pehla character:", first_char)
else:
    print("String empty hai!")
    
    
my_string = input("Apni string daalein: ")
if my_string:
    last_char = my_string[-1]  # -1 index = last character
    print("String ka last character:", last_char)
else:
    print("String empty hai!")
    
    
num = float(input("enter the mumber: "))
if num > 0:
    print("this number is positive.")
elif num < 0:
    print("this number is nagative.")
else:
    print("Number zero hai.")
    
    
num1 = float(input("Pehla number daalein: "))
num2 = float(input("Dusra number daalein: "))
num3 = float(input("Teesra number daalein: "))
sum_numbers = num1 + num2 + num3
print("In teeno numbers ka sum =", sum_numbers)  


user_input = input("enter your input: ")

print("The input you provided:", user_input)


    
    
    