print("Coding Exercise One")
liter = input("Input a number of liters: ")
def convert(liters):
    cubic_meters = 1000 * float(liters)
    return cubic_meters
print("There are ", convert(liter), " cubic meters in ", liter, " liters")

print("Coding Exercise Two")
password = input("Enter a password: ")
def strongorweak(password):
    strong = True
    if len(password) < 8:
        strong = False
    uppercase = False
    digit = False
    for i in password:
        if i.isupper():
            uppercase = True
        if i.isdigit():
            digit = True
    if uppercase == False:
        strong = False
    if digit == False:
        strong = False
    if strong == True:
        return "Strong Password"
    else:
        return "Weak Password"

print(strongorweak(password))
