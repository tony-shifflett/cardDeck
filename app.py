from flask import Flask, request, jsonify
import random

app = Flask(__name__)

cards = [
    "1H",
    "2H",
    "3H",
    "4H",
    "5H",
    "6H",
    "7H",
    "8H",
    "9H",
    "10H",
    "JH",
    "QH",
    "KH"
]

@app.route("/")
def test ():
    return "Basic Functionality Running"

@app.route('/deck')
def deck():
    newDeck = random.sample(cards, len(cards))
    return jsonify(newDeck)

@app.route('/unshuffled')
def unshuffled():
    return jsonify(cards)


if __name__ == '__main__':
    app.run(debug=True)