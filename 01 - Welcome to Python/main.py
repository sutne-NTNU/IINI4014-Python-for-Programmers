# Sivert Utne

# Promts user to enter his/her name, then saves it as a string
fullName = input("Hello! What is your full name?\nMy name is ")

# Splits the full name into an array with the individual names
names = fullName.split(" ")

# For each of the names, get the first character and adds it to the "initials" string then prints them.
initials = ""
for name in names:
    initials += name[0]
print("Your initials are: \"" + initials + "\"")

# Prints the welcome message
print("Welcome to Python " + fullName + "!")
