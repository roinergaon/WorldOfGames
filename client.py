import requests

# URL of the server
url = "http://localhost:5000/guess"

# Keep looping until the user guesses the right number
while True:
    # Get the guess from the user
    guess = int(input("Enter your guess: "))

    # Send the guess to the server
    response = requests.post(url, data={"guess": guess})

    # Check if the user has won the game
    if "Well done" in response.text:
        print(response.text)
        break

    # Print the result from the server
    print(response.text)
