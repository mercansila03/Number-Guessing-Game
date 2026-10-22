import random
play_again="yes"
number=random.randint(1,1000)
print("Guess my number between 1 and 1000")
guess=0
while(guess!=number):
    guess=int(input("Enter your guess: "))
    if guess>number:
        print("Too high! Try again.")
    elif guess<number:
        print("Too low! Try again.")
    else:
        print("Congratulations")
        break



