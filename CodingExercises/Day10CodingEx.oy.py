print("Coding Exercise One.")
try:
    total = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    print("That is ", (value / total) * 100, "%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero")
