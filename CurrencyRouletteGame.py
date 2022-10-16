from forex_python.converter import CurrencyRates

RANGE_MIN = 1
RANGE_MAX = 100


class CurrencyRouletteGame:

    def __init__(self, game_difficulty):
        self.game_difficulty = game_difficulty

    def get_money_interval(self):
        currency_interval = []
        c = CurrencyRates()
        currency = c.get_rate('USD', 'EUR')  # convert USD to EURO
        currency_interval.append(currency - (5 - self.game_difficulty))
        currency_interval.append(currency + (5 - self.game_difficulty))
        return currency_interval

    def get_guess_from_user(self):
        return input("Please guess the currency rate from USD to EUR between 1 to 100:")

    def play(self):
        currency_interval = self.get_money_interval()
        guess_from_user = self.get_guess_from_user()

        if currency_interval[0] <= float(guess_from_user) <= currency_interval[1]:
            print("User won")
            return True
        else:
            print("User lost")
            return False
