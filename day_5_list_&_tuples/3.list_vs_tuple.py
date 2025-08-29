#Difference between list and tuple

#List : mutable (you can mess with this)
number_list = ["1","2","3","4"]
print(number_list)
number_list[0] = "10"   #allowed
number_list.append("5") #allowed

print("list after cahnges :",number_list)

#tuple: immutable (you can't mess with this)
number_tuple = ("1","2","3","4")
print(number_tuple)
#number_tuple[0] = ("10")  #not allowed, will give error
#number_tuple.append("5")    #not allowed, will give error


#Use cases:
# Lists --> whenthe data may change 
# Tuple --> fixed data, faster, can de used as dictionary keys