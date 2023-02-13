from flask import Flask, request
import random

app = Flask(__name__)

# Generate a random number in the range [0, 100]
secret_number = random.randint(0, 100)

# Route for handling requests to the guessing game
@app.route("/guess", methods=["POST"])
def guess():
    # Get the user's guess from the request data
    guess = int(request.data)

    # Check if the guess is too high, too low, or correct
    if guess > secret_number:
        result = "Too big"
    elif guess < secret_number:
        result = "Too small"
    else:
        result = "Well done!"

    return result

if __name__ == "__main__":
    app.run()
