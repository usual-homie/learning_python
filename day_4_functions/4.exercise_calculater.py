# Exercise : Calculator using function

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        print("can't divide with 0")

print("Simple Calculator")

x = int(input("Enter your 1st no. :"))
y = int(input("Enter your 2nd no. :"))

print("Addition",add(x,y))
print("Subtracy",subtract(x,y))
print("Product",multiply(x,y))
print("Division",divide(x,y))