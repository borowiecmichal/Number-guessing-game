import random

number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number: "))
        if guess > number:
            print("Too big!")
        elif guess < number:
            print("Too small!")
        else:
            print("You won!!!")
            break
    except ValueError:
        print("It's not a number!")
        continue
