import random


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


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if secret_number == user_guess:
        print("You won! The number was {}".format(secret_number))
    else:
        print("You lost! The number was {}".format(secret_number))

    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "y":
        play(difficulty)
    else:
        print("Thank you for playing, see you next time!")
        return


if __name__ == "__main__":
    play()
