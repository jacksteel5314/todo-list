print("Coding Exercise One")
filenames = ['document', 'report', 'presentation']
for index, file in enumerate(filenames):
    row = f"{index}-{file.capitalize()}"
    print(row)

print("Coding Exercise Two")
ips = ["100.122.133.105", "100.122.133.111"]
index = int(input("Enter the index of the IP you want: "))
print("You chose ", ips[index])