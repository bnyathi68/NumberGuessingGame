import random

print("Welcome to this number guessing game")

top_of_range = input("To begin the game, please enter your top range number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please try a number greater than zero")
        quit()

else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Please enter a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if user_guess == random_number:
        print("You guessed correct!")
        break
    elif user_guess > random_number:
            print("Your guess is too high")
    else:
        print("Your guess is lower than actual")


print("You got in", guesses, "guesses")






