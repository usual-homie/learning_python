age = int(input("plz enter your age :"))

if age>=18:
    has_id = input("do you have any id (yes/no) :")

    if has_id.lower() == "yes":
        print("welcome to the club")
    elif has_id.lower() == "no":
        print("Sorry, you need an ID to enter the club")
    else:
        print("Invalid input")
else:
    print("Sorry, you're under 18. Not Allowed")