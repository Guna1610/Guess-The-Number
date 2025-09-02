from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
MEDIUM_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 4


turns = 0
# Function to check users guess against actual number.
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against """
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty level - 'easy' ,'medium' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'medium':
        return MEDIUM_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)

    print(f"the correct answer is {answer}")
    turns = set_difficulty()


    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess the number.
        guess = int(input("Make a Guess:"))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of guesses, you lose.")
            break
        elif guess != answer:
            print('Guess again.')

game()