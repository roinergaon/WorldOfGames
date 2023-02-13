from flask import Flask, request
import random
import sys

app = Flask(__name__)

# Generate a random number in range [0, 100]
secret = random.randint(0, 100)

@app.route("/guess", methods=["GET", "POST"])
def guess():
    # Get the guess from the client
    guess = int(request.form["guess"])

    # Check if the guess is too big, too small, or correct
    if guess > secret:
        result = "Too big."
    elif guess < secret:
        result = "Too small."
    else:
        result = "Well done! The secret number was " + str(secret)

    return result

if __name__ == "__main__":
    # Check if the correct number of arguments was provided
    if len(sys.argv) != 2:
        print("Usage: python server.py port")
        sys.exit()

    # Get the port from the command line argument
    port = int(sys.argv[1])

    # Start the server
    app.run(port=port)
