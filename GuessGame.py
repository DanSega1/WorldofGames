import random
from Score import Score

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty + 1)
    return secret_number


def get_guess_from_user(difficulty):
    user_guess = int(input("Please enter a number between 1 to {}: ".format(difficulty+1)))
    return user_guess


def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False


def play(difficulty, username):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if secret_number == user_guess:
        game_name = "Guess Game"
        score_manager = Score()
        new_txt_score, new_csv_score = score_manager.add_score(game_name, difficulty, username)
        print("You won! The number was {}".format(secret_number))
        print(f"Your global score is: {new_txt_score} pt")
        print(f"Your score in {game_name} is: {new_csv_score} pt")
    else:
        print("You lost! The number was {}".format(secret_number))

    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "y":
        play(difficulty, username)
    else:
        print("Thank you for playing, see you next time!")
        return


if __name__ == "__main__":
    play(difficulty=1)
