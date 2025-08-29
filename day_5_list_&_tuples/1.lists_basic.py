#basic list operations
#they are inside large brackets [""]
fruits = ["applle","banana","cherry"]


#accessing elements
print(fruits[0]) #for left to right it starts from zero(0) then 1 then 2 and so on
print(fruits[-1]) #for right to left it starts form negative -1 then -2 and so on


#adding elements
fruits.append("orange") #basically .append("anything you want to add in the ist") add the element at the end of th list
print("after append :", fruits)

#removing element
fruits.remove("banana")
print("after removing :", fruits)

#printing through loop now
for i in fruits:
    print(i)