#Managing a shoping list

#start with a empty list
shopping_list = []

#add 3 items from user input

for i in range(3):
    item = input(f"Enter item {i+1} : ")
    shopping_list.append(item)

print("your shopping list", shopping_list)

#showing the first and last item in list
print("first item in your list",shopping_list[0])
print("last item in your list", shopping_list[-1])

#converting list into tuple(immutable version)
shopping_list = tuple(shopping_list)
print("immutable tuple version : ", shopping_list)