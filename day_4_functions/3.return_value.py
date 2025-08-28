#function with return a value

def add(a,b):
    return a + b

def multiply(a,b):
    return a*b

#using the function
x = int(input("Enter the first no. :" ))
y = int(input("Enter the second no. :"))

print("Sum :",add(x,y))
print("Product :",multiply(x,y))