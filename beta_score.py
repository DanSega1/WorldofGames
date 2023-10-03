import os
import Score
from prettytable import PrettyTable
import csv
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
    # Check if the file exists and is empty, write the header if needed
    if not os.path.isfile('scoreboard.csv') or os.stat('scoreboard.csv').st_size == 0:
        with open('scoreboard.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Game Name", "Score"])

    # Collect data into the CSV file
    with open('scoreboard.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, game_name, score])


def read_data_from_csv():
    scoreboard = create_scoreboard()
    with open('score.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row (header)
        for row in reader:
            scoreboard.add_row(row)
    return scoreboard


display_scoreboard(read_data_from_csv())
