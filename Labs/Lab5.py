import random

"""
Write a 'guess the number game' where a random number is generated and the user 
 must guess the number. The program says if their number is too high or too low 
 until the right answer is guessed.
"""

print("Welcome to the guessing game! Please guess a number between 1-20")
# Generate random number between 1-20
randomN = int(random.randint(1, 20))

while True:
    try:
        # print("Welcome to the guessing game! Please guess a number between 1-20")
        # commented the line out above so the while loop does not repeat "Welcome.."
        guess = int(input())
    
        if guess == randomN:
            print("Congrats! You got the number *finally*! The number was %s." % randomN)
            break

        elif guess > randomN:
            print("Sorry! You guessed incorrectly. The number is lower.")

        elif guess < randomN:
            print("Sorry! You guessed incorrectly. The number is higher.")

    except:
        print("Well... all you had to do was guess a number.")