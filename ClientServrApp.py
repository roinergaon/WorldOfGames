from flask import Flask, request, render_template
import random
import sys

app = Flask(__name__)

# Welcome message for the user
@app.route('/')
def welcome():
    return render_template('number_guesser.html')

# Generate a random number in the range provided by the user
@app.route('/range', methods=['POST'])
def set_range():
    global secret, lower, upper
    lower = int(request.form['lower-bound'])
    upper = int(request.form['upper-bound'])
    secret = random.randint(lower, upper)
    return render_template('number_guesser.html', lower=lower, upper=upper)

# Get the user's guess and compare it to the secret number
@app.route('/guess', methods=['POST'])
def guess():
    global secret
    guess = int(request.form['guess'])
    if guess > secret:
        return "Too big"
    elif guess < secret:
        return "Too small"
    else:
        return "Well done"

# Check if the number of arguments passed through sys.args is correct
if len(sys.argv) != 3:
    print("Usage: python number_guesser.py PORT TEMPLATE_DIR")
    sys.exit()

# Start the Flask server
if __name__ == '__main__':
    app.run(port=int(sys.argv[1]), template_folder=sys.argv[2], debug=True)
