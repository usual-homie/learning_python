# Dictionaries methods

students = {
    "name" : "Arcan",
    "age" : 23,
    "course" : "Python"
}

# Get all keys
print("Keys :", students.keys())


# Get all Values
print("Values :", students.values())


# Get key-value pairs
print("Items", students.items())


# Use get() to safely access a value
print("Name (using get) :", students.get("name"))
print("Grade (using get) :", students.get("grade","not found")) #default value if the key doesn't exist


# Update dictionary with another dictonary
students.update({"grade" : "A", "age" : "24"})

print("Updated dictionary", students)


# Removing an item with pop()
removed = students.pop("course", "No course found")
print("Removed", removed)


# Clear the dictionary
students.clear()
print("Cleared students", students)