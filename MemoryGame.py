import random
import time


def generate_sequence(game_difficulty):
    randomlist = []
    for i in range(game_difficulty):
        n = random.randint(1, 101)
        randomlist.append(n)

    print(randomlist)
    time.sleep(0.7)
    print("\n" * 40)

    return randomlist


def get_list_from_user(game_difficulty):
    userlist = []
    for i in range(game_difficulty):
        n = input("Enter numbers you have remember:")
        userlist.append(int(n))
    return userlist


def is_list_equal(randomlist, list_from_user):
    randomlist.sort()
    list_from_user.sort()
    if randomlist == list_from_user:
        return True
    else:
        return False


def play(game_difficulty):
    randomlist = generate_sequence(game_difficulty)
    userlist = get_list_from_user(game_difficulty)
    result = is_list_equal(randomlist, userlist)
    if result:
        print("User won")
        return True
    else:
        print("User lost")
        return False
