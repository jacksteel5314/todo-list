import glob
import csv
import shutil
import webbrowser

# Prints Files in Current Folder
myfiles = glob.glob("*.txt")
print(myfiles)

# Prints files in bonus Folder
thefiles = glob.glob("bonus/*.txt")
print(thefiles)

# Prints Contents of Each File in myfiles
for filepath in thefiles:
    with open(filepath, "r") as file:
        print(file.read())

with open("../venv/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")
for row in data:
    if row[0] == city:
        print(row[1])

# Makes Zip Files
shutil.make_archive("output", "zip", "../venv/files")

user_term = input("Enter a search term: ").replace(" ", "+")
webbrowser.open("https://google.com/search?q=" + user_term)