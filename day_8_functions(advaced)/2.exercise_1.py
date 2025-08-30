# Write a function called make_profile that takes in:
# name (required)
# age (required)
# city (default = "Unknown")
# hobby (default = "None")

def make_profile(name, age, city = "Unknown", hobby = "None"):
    print("Name :", name, "Age :", age, "City :", city, "Hobby :", hobby)

make_profile("Arcan", 23)
make_profile("Sara", 25, "Paris", "Painting")
make_profile("Leo", 30, "Rome")
make_profile(age=18, name="Alex") #no matter the order if we give proper arguments iy'll pick up