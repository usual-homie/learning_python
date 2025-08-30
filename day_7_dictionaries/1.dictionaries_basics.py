# Dictionaries in python (key-value pairs)

#creating a dictionary
students = {
    "name" : "Arcan",
    "age" : "23",
    "course" : "Python"
}

# Access value
print("Name :", students["name"])
print("Age :", students["age"])
print("Course :", students["course"])

# Adding a value
students["grade"] = "A"

# Upadting a value
students["age"] = "24"

# Deleting a key-value pair
del students["course"]

# Printing updated dictionary
print("Updated student dictionary value", students)