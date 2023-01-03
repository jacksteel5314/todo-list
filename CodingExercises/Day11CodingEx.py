print("Coding Exercise One")
grades = [9.6, 9.2, 9.7]
newgrades = []
for i in grades:
    newgrades.append(float(i))
def get_max():
    return max(newgrades)
print(get_max())

print("Coding Exercise Two")
def get_maxmin():
    return "Max: " + str(max(newgrades)) + ", Min: " + str(min(newgrades))
print(get_maxmin())
