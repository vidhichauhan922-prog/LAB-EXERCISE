src=open("d1.txt","r")
data=src.read()
src.close()

dst=open("BSCIT.txt","w")
dst.write(data)
dst.close()
print("file copied successfully")



with open("d1.txt","r")as f1:
    data=f1.read()

with open("BSCIT.txt","w")as f2:
    f2.write(data)
        
print("content copied successfully!")



with open("d1.txt","r")as f:
    data=f.read()

print("Total characters:",len(data))



with open("d1.txt","r")as f1:
    data=f1.read()

with open("upeer.txt","w")as f2:
    f2.write(data.upper())

print("converted to uppercase!!")



with open("d1.txt","r")as f:
    first_line=f.readline()

print("First line :",first_line)