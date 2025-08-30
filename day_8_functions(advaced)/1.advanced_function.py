#function with default argument

# example 1

def greet(name="Programmer"):
    print("Hello", name)

greet("Arcan")
greet()

# example 2

def power(base,exponent=2):
    return base ** exponent
print(power(5))
print(power(5,3))

# example 3

def order_coffe(type="hot"):
    print("Here is your", type, "coffee")

order_coffe()
order_coffe("iced")

# example 4

def add_to_cart(item, quantity=1, delivery="standard"):
    print(quantity, item, "added with", delivery, "delivery")

add_to_cart("laptop")

add_to_cart("book",1,"express")