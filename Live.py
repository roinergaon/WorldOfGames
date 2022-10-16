from CurrencyRouletteGame import CurrencyRouletteGame
from GuessGame import play as PlayGuessGame
from MemoryGame import play as PlayMemoryGame
#from CurrencyRouletteGame import play as PlayCurrencyRouletteGame, CurrencyRouletteGame
from Score import Add_score


def welcome(name):
    print("Hello " + name + " and welcome to the World of Games(WoG).\n" +
          "Here you can find many cool games to play.")


def load_game():
    choosen_game = input("Please choose a game to play:\n" +
                         "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n" +
                         "2. Guess Game - guess a number and see if you chose like the computer.\n" +
                         "3. Currency Roulette - try and guess the value of a random amount of USD in EUR.\n")

    while not choosen_game.isnumeric() or int(choosen_game) < 1 or int(choosen_game) > 3:
        choosen_game = input("Please enter value between 1 - 3\n")

    game_difficulty = input("Please choose game difficulty from 1 to 5:\n")
    while not game_difficulty.isnumeric() or int(game_difficulty) < 1 or int(game_difficulty) > 5:
        game_difficulty = input("Please enter value between 1 - 5\n")

    if int(choosen_game) == 1:
        win_lost = PlayMemoryGame(int(game_difficulty))
    elif int(choosen_game) == 2:
        win_lost = PlayGuessGame(int(game_difficulty))
    else:
        currency_roulette_game = CurrencyRouletteGame(int(game_difficulty))
        if currency_roulette_game.play():
            print("\nYou won the game!")
            Add_score(int(game_difficulty))
        else:
            print('\nYou lost the game, I wish you better luck next time.')
       # win_lost = PlayCurrencyRouletteGame(int(game_difficulty))

    #if win_lost:
     #Add_score(int(game_difficulty))