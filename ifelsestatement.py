import random
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number:
    print ("well done.")
if guess < secret_number:
    print ("too low")
if guess > secret_number:
    print ("too high")