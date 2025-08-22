marks = int(input("Enter your marks(0-100) :"))

if marks>=90:
    print("Grade O")
elif marks>=80:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=50:
    print("Grade D")
elif marks>=40:
    print("Grade E")
elif marks<40:
    print("Grade F")
else:
    print("invalid input")
