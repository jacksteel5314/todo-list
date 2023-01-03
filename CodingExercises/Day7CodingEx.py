print("Coding Exercise One")
names = ["john smith", "jay santi", "eva kuki"]
capitalized = [name.title() for name in names]
print(capitalized)

print("Coding Exercise Two")
usernames = ["john1990", "alberta1970", "magnola2000"]
nums = [len(username) for username in usernames]
print(nums)

print("Coding Exercise Three")
user_entries = ["10", "19.1", "20"]
user_floats = [float(entry) for entry in user_entries]
print(user_floats)

print("Coding Exercise Four")
user_floats = [float(entry) for entry in user_entries]
summer = sum(user_floats)
print(summer)

