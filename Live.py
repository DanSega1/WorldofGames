def welcome(name):
    hello = (f"Hello {name} and welcome to the World of Games (WoG).\n"
             f"Here you can find many cool games to play.")
    return hello


def load_game():
    global game_chooser, difficulty
    too_much = "The number you chose is not in range"
    not_int = "Invalid input, please enter a number"
    is_valid_input = False

    while is_valid_input is False:
        game_chooser = input(
            f"Please choose a game to play: (To choose type the number of the game and press enter)\n"
            f"1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
            f"2. Guess Game - guess a number and see if you chose like the computer\n"
            f"3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
            f"q. To quit\n")
        try:
            game_chooser = int(game_chooser)
            if isinstance(int(game_chooser), int) and 1 <= int(game_chooser) <= 3:
                is_valid_input = True
            else:
                print(too_much)
        except ValueError:
            print(not_int)

    is_valid_input = False
    while is_valid_input is False:
        difficulty = input(f"Please choose game difficulty from 1 to 5: \n")
        try:
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:
                is_valid_input = True
            else:
                print(too_much)
        except ValueError:
            print(not_int)

    result = {"game_chooser": game_chooser,
              "difficulty": difficulty}
    return result


def open_game(game_chooser, difficulty):
    if game_chooser == 1:
        from MemoryGame import play
        return play(difficulty)
    elif game_chooser == 2:
        from GuessGame import play
        return play(difficulty)
    elif game_chooser == 3:
        from CurrencyRouletteGame import play
        return play(difficulty)
    elif game_chooser == "q":
        print("Thank you for playing, see you next time!")
        return


def main():
    while True:
        game_data = load_game()
        game_chooser = game_data["game_chooser"]
        difficulty = game_data["difficulty"]
        open_game(game_chooser, difficulty)