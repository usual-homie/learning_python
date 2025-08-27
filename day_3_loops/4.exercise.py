#3you don't have to use any random command yet so skip it(i'm using it for fun only cuz i'm bored)
import random

#since you're not using import random so just give secret any int you want lik: secret = 6 that's it
secret = random.randint(1,10)

attempts = 3
print("you have to guess the number between 1 to 10, you have 3 attempts")

while attempts > 0:
    guess = int(input("Guess the number(1-10) :"))

    if guess == secret:
        print("bravo! you guessed it righ, you win")
        break
    else:
        print("you guessed it wrong try again")
        attempts-=1
if attempts == 0:
    print("you're out of attempts, you lost. the number was",secret)