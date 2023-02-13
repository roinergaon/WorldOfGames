from flask import Flask, request, render_template
import random
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('number_guesser.html')

# Welcome message for the user
@app.route('/')
def welcome():
    return "Welcome to the number guessing game!\nGuess a number between 0 and 100."

# Generate a random number in the range [0-100]
secret = random.randint(0, 100)

# Get the user's guess and compare it to the secret number
@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if guess > secret:
        return "Too big"
    elif guess < secret:
        return "Too small"
    else:
        return "Well done"

# Check if the number of arguments passed through sys.args is correct
if len(sys.argv) != 2:
    print("Usage: python number_guesser.py PORT")
    sys.exit()

# Start the Flask server
if __name__ == '__main__':
    app.run(port=int(sys.argv[1]), debug=True)
