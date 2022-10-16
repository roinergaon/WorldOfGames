import random


def generate_number(game_difficulty):
    secret_number = random.randint(0, game_difficulty)
    return secret_number


def get_guess_from_user(game_difficulty):
    guess_from_user = input("Please guess a number from 1 to " + str(game_difficulty))
    while int(guess_from_user) < 1 or int(guess_from_user) > game_difficulty:
        guess_from_user = input("You entered wrong value please enter again:")
    return guess_from_user


def compare_results(secret_number, guess_from_user):
    if guess_from_user == secret_number:
        return True
    else:
        return False


def play(game_difficulty):
    secret_number = generate_number(game_difficulty)
    guess_from_user = get_guess_from_user(game_difficulty)
    result = compare_results(secret_number, int(guess_from_user))
    if result:
        print("User won")
        return True
    else:
        print("User lost")
        return False

    # return compare_results(generate_number(game_difficulty), get_guess_from_user(game_difficulty))
