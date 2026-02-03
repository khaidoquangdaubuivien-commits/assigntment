import random
print("Guess a random integer between 1 and 10")

x = random.choice([1,2,3,4,5,6,7,8,9,10])

while True:
    guess = int(input("Guess a number: "))

    if guess == x:
        print("Correct!")
        break

    if guess < x:
        print("Too low!")

    elif guess > x:
        print("Too high!")



