

def clear_screen():
    print("\n" * 50)


def write_score_board():
# write the score board to scrote.txt from all of the games
    score = open("score.txt", "w")
    score.write("Memory Game - {} attempts, {} seconds\n".format(memory_game["attempts"], memory_game["time"]))
    score.write("Guess Game - {} attempts, {} seconds\n".format(guess_game["attempts"], guess_game["time"]))
    score.write("Currency Roulette - {} attempts, {} seconds\n".format(currency_roulette_game["attempts"], currency_roulette_game["time"]))
    score.close()


def show_score_board():
    score = open("score.txt", "r")
    print(score.read())
    score.close()

