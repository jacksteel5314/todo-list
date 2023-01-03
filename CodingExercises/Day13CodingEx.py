print("Coding Exercise One")
def function(year_of_birth, current_year = 2022):
    age = int(current_year) - int(year_of_birth)
    return age

user_input = int(input("What year were you born? "))
theage = function(user_input)
print("You are ", function(user_input), " years old!")
if theage > 120:
    print("Wow, you are very old.")


print("Coding Exercise Two")
list = input("Enter names separated by commas (no spaces): ")
splitList = list.split(",")
print("You gave me ", len(splitList), " names")
