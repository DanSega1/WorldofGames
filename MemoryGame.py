import random
import time
import Utils
# from Score import add_score


def display_numbers(numbers, duration):
    print("Remember these numbers:")
    print(" ".join(map(str, numbers)))
    time.sleep(duration)
    Utils.clear_screen()


def generate_sequence(difficulty):
    generated_list = []
    for i in range(difficulty):
        generated_list.append(random.randint(1, 101))
    return generated_list


def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
        user_list.append(int(input("Please enter a number: ")))
    return user_list


def is_list_equal(generated_list, user_list):
    if generated_list == user_list:
        return True
    else:
        return False


def play(difficulty):
    generated_list = generate_sequence(difficulty)
    print(generated_list)
    user_list = get_list_from_user(difficulty)
    print(user_list)
    if generated_list == user_list:
        print("You won!")
        # add_score(difficulty)
    else:
        print("You lost!")
    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "y":
        play(difficulty)
    else:
        print("Thank you for playing, see you next time!")
        return


# def display_numbers(numbers, duration):
#     print("Remember these numbers:")
#     print(" ".join(map(str, numbers)))
#     time.sleep(duration)
#     clear_screen()


def get_user_guess():
    guess = input("Enter your guess (separated by spaces): ")
    return list(map(int, guess.strip().split()))


def main(difficulty):
    random_numbers = random.sample(range(1, 101), difficulty)

    display_duration = 0.7
    display_numbers(random_numbers, display_duration)

    user_guess = get_user_guess()

    if user_guess == random_numbers:
        print("Congratulations! You guessed correctly!")
    else:
        print("Sorry, your guess was incorrect. The correct numbers were:")
        print(" ".join(map(str, random_numbers)))


if __name__ == "__main__":
    main(3)
