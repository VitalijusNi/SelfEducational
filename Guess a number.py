import random
import math


rand_number = random.randrange(11)
while True:
    try:
        secret_number = int(input("Guess a number between 1 and 10: "))
        if secret_number == rand_number:
            break
        elif secret_number < rand_number:
            print("Little bit more")
        elif secret_number > rand_number:
            print("Little bit less")
    except ValueError:
        print("Please enter a number")

print("You guessed correct")