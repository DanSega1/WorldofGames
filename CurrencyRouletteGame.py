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

# import random
# from Live import open_game
# import requests
#
# access_key = "90255cc2b8da350406d10cbecba25795"
#
#
#
# def get_money_interval(difficulty):
#     response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
#     data = response.json()
#     usd_to_ils = data["rates"]["ILS"]
#     total_value_of_money = random.randint(1, 100)
#     interval = (total_value_of_money - (5 - difficulty), total_value_of_money + (5 - difficulty))
#     return interval
#
#
#
#
# def play(difficulty):
#     secret_number = generate_number(difficulty)
#     user_guess = get_guess_from_user(difficulty)
#     return compare_results(secret_number, user_guess)

import requests
import random

class CurrencyGuessGame:
    def __init__(self, access_key):
        self.difficulty = 1
        self.total_value_of_money = 0
        self.access_key = "90255cc2b8da350406d10cbecba25795"

    def get_money_interval(self):
        url = f'https://api.exchangeratesapi.io/latest?base=USD&symbols=ILS&access_key={self.access_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            exchange_rate = data['rates']['ILS']
            lower_bound = self.total_value_of_money - (5 - self.difficulty)
            upper_bound = self.total_value_of_money + (5 - self.difficulty)
            return lower_bound * exchange_rate, upper_bound * exchange_rate
        else:
            raise Exception("Failed to get exchange rate data. Please try again later.")

    # Other methods remain unchanged...
CurrencyGuessGame()