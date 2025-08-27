#WAP to show ticket cost for kids under 5 it's free for child under 18 it's 100 for adult it's 200 and with student pass it's 150 and last for Senior citizen it's 120

age = int(input("Enter your age :"))

if age<0 or age >120:
    print("Enter a valid age")
elif age < 5:
    print("you're free to go kiddo")
elif age < 18:
    print("child ticket : 100")
elif age < 60:
    has_id = input("Do you have Student Id (yes/no) :")
    if has_id.lower() == "yes":
        print("student discount ticket charge: 150")
    else:
        print("adult ticket : 200")
else:print("Senior ticket : 120")