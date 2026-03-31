
with open("d1.txt", "r") as f1, open("BSCIT.txt", "w") as f2:
    char = f1.read(1)
    while char:

        f2.write(char)
        char = f1.read(1)
        print("file coppied successfully")



with open("d1.txt", "r") as f1, open("BSCIT.txt", "w") as f2:
    for line in f1:
        f2.write(line)

        print("coppied successfully")



lines_list = ["Apple\n", "Banana\n", "Cherry\n"]
with open("BSCIT.txt", "w") as f:
    f.writelines(lines_list)
    
    print("PLAN SUCCESSFULL")



with open("d1.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"Line number: {i}\n")

        print("all done")



user_text = input("what you want to write?: ")

with open("d1.txt", "a") as f:
    f.write(user_text)
    print("data is saved!")


with open("BSCIT", "a") as f:
    print("write your 5 words:")
    for i in range(5):
        line = input(f"Line {i+1}: ")
        f.write(line + "\n")

print("SAVE YOUR WORDS")








