import csv
from Score import Score  # Import the Score class from your Score.py module
from prettytable import PrettyTable
import pyfiglet
from colorama import Fore, Style


def create_scoreboard():
    # Create a PrettyTable for the scoreboard
    table = PrettyTable()
    table.field_names = ["     Username     ", "     Game Name     ", "     Score     "]
    return table


def display_scoreboard(table):
    # Display the scoreboard with a colored Figlet title (slant font)
    figlet = pyfiglet.Figlet(font='slant')
    figlet_title = f"{Fore.YELLOW}{figlet.renderText(' Scoreboard')}{Style.RESET_ALL}"

    print(figlet_title)
    print(table)


def collect_data(username, game_name, score):
    # Initialize the Score class
    score_manager = Score()

    # Use the add_score_csv method to collect data into the CSV file
    score_manager.add_score_csv(game_name, score, username)


def read_data_from_csv():
    while True:
        scoreboard = create_scoreboard()

        # Initialize the Score class
        score_manager = Score()

        # Use the update_score method to read data from the CSV file
        with open(score_manager.csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first row (header)
            for row in reader:
                scoreboard.add_row(row)

        display_scoreboard(scoreboard)  # Display the scoreboard

        choice = input("Press 'q' to return to the Live menu or 'Enter' to refresh the scoreboard: ").strip().lower()

        if choice == 'q':
            break  # Return to the Live menu


if __name__ == "__main__":
    display_scoreboard(read_data_from_csv())
