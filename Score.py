import csv


class Score:
    def __init__(self, txt_file_path='score.txt', csv_file_path='score.csv'):
        self.txt_file_path = txt_file_path
        self.csv_file_path = csv_file_path

    def add_score_txt(self, difficulty):
        try:
            # Try to read the current score from the TXT score file
            with open(self.txt_file_path, 'r') as file:
                current_score = int(file.read().strip())
        except FileNotFoundError:
            # If the TXT score file doesn't exist, create it with an initial score of 0
            current_score = 0
            with open(self.txt_file_path, 'w') as file:
                file.write(str(current_score))

        # Calculate the new score based on the difficulty
        new_score = current_score + (difficulty * 3) + 5

        # Update the TXT score file with the new score
        with open(self.txt_file_path, 'w') as file:
            file.write(str(new_score))

        return new_score

    def add_score_csv(self, game_name, difficulty, username):
        try:
            # Try to read the current score from the CSV scores file
            with open(self.csv_file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    if row[0] == username and row[1] == game_name:
                        current_score = int(row[2])
                        break
                else:
                    # If the user's data isn't found, create a new record with an initial score of 0
                    current_score = 0

        except FileNotFoundError:
            # If the CSV scores file doesn't exist, create it with a header
            current_score = 0
            with open(self.csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["username", "game_name", "score"])

        # Calculate the new score based on the difficulty
        new_score = current_score + (difficulty * 3) + 5

        # Update the CSV score file with the new score or create a new record
        with open(self.csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, game_name, new_score])

        # Update the TXT score file with the new score
        with open(self.txt_file_path, 'w') as txt_file:
            txt_file.write(str(new_score))

        return new_score

    def add_score(self, game_name, difficulty, username):
        # Call both TXT and CSV score update methods
        txt_score = self.add_score_txt(difficulty)
        csv_score = self.add_score_csv(game_name, difficulty, username)

        # Return both scores
        return txt_score, csv_score


if __name__ == "__main__":
    score = Score()
    difficulty = 3  # Replace with the actual difficulty value
    username = "daniel"  # Replace with the actual username value
    game_name = "Memory Game"  # Replace with the actual game name value
    new_txt_score, new_csv_score = score.add_score(game_name, difficulty, username)
    print(f"New TXT score: {new_txt_score}")
    print(f"New CSV score: {new_csv_score}")