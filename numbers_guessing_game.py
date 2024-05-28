import random

def numbers_game():
    answer = random.randint(0, 100)
    guess_limit = 10
    guesses_taken = 0

    while guesses_taken < guess_limit:
        user_guess = int(input("What is your guess? > "))
        guesses_taken += 1

        if user_guess == answer:
            print(f"Corrent! The answer is {user_guess}")
            break

        if user_guess < answer:
            print(f"{user_guess} is too low!")
        else:
            print(f"{user_guess} is too high!")

        if guesses_taken == guess_limit:
            print(f"No more guesses. The Correct Answer was {answer}")

numbers_game()