# Phonebook dictionary exercise

phonebook = {}

while True :
    print("\n--- Phonebook Menu ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search conatct")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = int(input("\n Enter your choice (1-5) :"))

    if choice == 1:
        name = input("plz enter the name :")
        number = input("plz enter the number :")
        phonebook[name] = number
        print("contact saved")

    elif choice == 2:
        if phonebook:
            for name, number in phonebook.items():
                print(name, ":", number )
        else:
            print("no contacts are saved it")

    elif choice == 3:
        name = input("Enter the name yoiu want to search :")
        print("Number :", phonebook.get(name,"Not found"))

    elif choice == 4:
        name = input("Enter the name to delete :")
        removed = phonebook.pop(name, None)

        if removed:
            print("Deleted contact", name)
        else:
            print("contact not found")
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("invalid choice, try again")