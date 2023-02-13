import sys
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/s', methods=['GET', 'POST'])
def index():
    message = "Welcome to the number guessing game!"
    secret = random.randint(0, 100) if len(sys.argv) < 2 else random.randint(0, int(sys.argv[1]))
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess == secret:
            message = "Well done! The secret number was {}".format(secret)
        elif guess > secret:
            message = "Too big! Try again."
        else:
            message = "Too small! Try again."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()

