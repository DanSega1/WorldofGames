"""This game will use the free currency api to get the current exchange rate from USD to ILS, will
generate a new random number between 1-100 a will ask the user what he thinks is the value of
the generated number from USD to ILS, depending on the user’s difficulty his answer will be
correct if the guessed value is between the interval surrounding the correct answer

Properties
1. Difficulty
Methods
1. get_money_interval -Will get the current currency rate from USD to ILS and will
generate an interval as follows:
a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
(5 - d))

2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
value to a given amount of USD
3. play - Will call the functions above and play the game. Will return True / False if the user
lost or won."""
import random
import requests
from Score import Score

# work
def exchange_rate_api():
    # For now, I will use a free API to get the exchange rate data of EUR to ILS
    url = "http://api.exchangeratesapi.io/v1/latest?access_key=90255cc2b8da350406d10cbecba25795&symbols=ILS"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['rates']['ILS']
        return exchange_rate
    else:
        raise Exception("Failed to get exchange rate data. Please try again later.")


# --------------------------------------------------------------------

def get_guess_from_user(total_value):
    guess = float(input(f"Guess the value of {total_value} EUR in ILS: "))
    return guess


def get_money_interval(difficulty, exchange_rate):
    total_value = random.randint(1, 100)  # Generate a random total value of money
    interval = (total_value - (5 - difficulty) * exchange_rate,
                total_value + (5 - difficulty) * exchange_rate)
    return total_value, interval


def play(difficulty, username):
    exchange_rate = exchange_rate_api()
    total_value, interval = get_money_interval(difficulty, exchange_rate)
    user_guess = get_guess_from_user(total_value)

    if interval[0] <= user_guess <= interval[1]:
        game_name = "Currency Roulette"
        score_manager = Score()
        new_txt_score, new_csv_score = score_manager.add_score(game_name, difficulty, username)
        print("Congratulations! Your guess is within the correct range.\n"
              "The correct answer is: {:.2f} ILS".format(total_value * exchange_rate))
        print(f"Your global score is: {new_txt_score} pt")
        print(f"Your score in {game_name} is: {new_csv_score} pt")
    else:
        print("Sorry, your guess is not within the correct range.\n"
              "The correct answer is: {:.2f} ILS".format(total_value * exchange_rate))

    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "y":
        play(difficulty, username)
    else:
        print("Thank you for playing, see you next time!")
        return


def main(difficulty):
    exchange_rate = exchange_rate_api()
    game = play(difficulty, exchange_rate)

    result = game.play()
    if result:
        print("You won!")
    else:
        print("You lost!")


if __name__ == "__main__":
    play(difficulty=1)
