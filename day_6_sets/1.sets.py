# sets in python
# - Unorded collection of unique item
# - No duplicates allowed

# Creating a set
fruits = {"apple","banana","cherry","apple"}
print("Set :",fruits) # duplicates are removed 

# adding elements
fruits.add("pulm")
print("set after adding element", fruits)

# Removing elements
fruits.remove("banana")
print("set after removing an element ",fruits)

# Membership test
print("is apple in the set ? :", "apple" in fruits)

# set operation
A = {"1","2","3","4"}
B = {"3","4","5","6"}

print("Union", A | B)
print("Intersection", A & B)
print("Difference (A-B)", A - B)
print("Symetric Differnce", A ^ B)