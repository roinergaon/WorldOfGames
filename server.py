from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/")
def guess():
    lower = 0
    upper = 100
    secret_number = random.randint(lower, upper)
    message = "The secret number is in the range [" + str(lower) + "-" + str(upper) + "].\n"

    if request.args.get("guess"):
        guess = int(request.args.get("guess"))
        if guess > secret_number:
            message += "Too big\n"
        elif guess < secret_number:
            message += "Too small\n"
        else:
            message += "Well done!\n"

    return message

if __name__ == "__main__":
    app.run()
