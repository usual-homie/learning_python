# Exercise : Sets in Python

# Q1 : Create two sets on numbers: even and odd. (from 1 to 10)
# Print their Union and Intersection.

evens = {2,4,6,8,10}
odds = {1,3,5,7,9}

print("Union of evens and odds", evens | odds)
print("Intersection of evens and oods", evens & odds)

# Q2: Create a set of vowels and check if user input is a vowel.

vowels = {"a","e","i","o","u"}
letter = str(input("Enter a char from aplphabet :").lower())

if letter in vowels:
    print(letter,"is a vowel")
else:
    print(letter,"is not a vowel")