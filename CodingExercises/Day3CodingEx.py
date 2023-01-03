print("Coding Exercise 1")
country = input("Input the country you are from: ")
match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")

print("Coding Exercise 2")
ingredients = ["john smith", "sen plakay", "dora ngacely"]
for i in ingredients:
    print(i.title())
