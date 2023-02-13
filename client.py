import requests

def play_guessing_game(host):
    url = "http://" + host
    message = requests.get(url).text
    print(message, end="")
    guess = int(input("Make a guess: "))
    url += "?guess=" + str(guess)
    message = requests.get(url).text
    print(message, end="")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python guessing_game_client.py host")
        sys.exit(1)

    host = sys.argv[1]
    play_guessing_game(host)
