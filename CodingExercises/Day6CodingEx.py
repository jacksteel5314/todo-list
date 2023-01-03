print("Coding Exercise One")
file = open(f"../files/essay.txt", "r")
theMessage = file.readlines()
file.close()
for word in theMessage:
    print(word.title())

print("Coding Exercise Two")
sum = 0
for word in theMessage:
    sum = sum + len(word)
print(sum)

print("Coding Exercise Three")
member = input("Add a new member: ")
filez = open(f"../files/members.txt", "r")
existing_members = filez.readlines()
filez.close()
existing_members.append(member + "\n")
filez = open(f"../files/members.txt", "w")
existing_members = filez.writelines(existing_members)
filez.close()

print("Coding Exercise Four")
filenames = ["doc.txt", "report.txt", "presentation.txt"]
for filename in filenames:
    filo = open(f"../files/{filename}", "w")
    filo.write("Hello")

print("Coding Exercise Five")
afile = open(f"../files/a.txt", "r")
aread = afile.readlines()
afile.close()
for a in aread:
    print(a)
bfile = open(f"../files/b.txt", "r")
bread = bfile.readlines()
bfile.close()
for b in bread:
    print(b)
cfile = open(f"../files/c.txt", "r")
cread = cfile.readlines()
cfile.close()
for c in cread:
    print(c)
