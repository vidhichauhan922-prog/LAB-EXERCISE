password = ""

while password != "secret123":
    password = input("Enter the correct password: ")
    if password != "secret123":
        print("Wrong! Try again.")

print("Access Granted!")


timer = 5
while timer > 0:
    print(timer, "...")
    timer -= 1
print("Blast off! ")


total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print("The total sum is:", total)


total = 0
num = 1
while num <= 20:
    total += num
    num += 1
print("The total sum is:", total)


i = 1
while i <= 10:
    if i % 2 == 0:
        print(i, "is even")
    i += 1


i = 1
while i <= 20:
    if i % 2 == 0:
        print(i, "is even")
    i += 1


i = 1
while i <= 10:
    if i % 2 != 0:
        print(i, "is odd")
    i += 1


i = 1
while i <= 20:
    if i % 2 != 0:
        print(i, "is odd")
    i += 1


i=1
while i<=5:
    print(i)
    i=i+1

i=1
while i<=50:
    print(i)
    i=i+1


n = int(input("enter n:"))
i=1
s=0
while i <= n:
    s=s+i
    i=i+1
    print("sum",s)


