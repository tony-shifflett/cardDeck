from flask import Flask, request, jsonify
import random

app = Flask(__name__)

#lists containing card data
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Clubs", "Spades", "Diamonds"]


def createDeck ():
    newDeck = []
    for value in values:
        for suit in suits:
            newCard =[]
            newCard.append(value)
            newCard.append(suit)
            newDeck.append(newCard)
    return newDeck


@app.route("/")
def test ():
    return "Basic Functionality Running"

@app.route('/deck')
def deck():
    newDeck = createDeck()
    random.shuffle(newDeck)
    return jsonify(newDeck)

@app.route('/deck/jokers')
def jokerDeck():
    newDeck = createDeck()
    random.shuffle(newDeck)
    newDeck.insert(random.randint(0, len(newDeck)),["Joker", "Joker"])
    newDeck.insert(random.randint(0, len(newDeck)),["Joker", "Joker"])
    return jsonify(newDeck)

@app.route('/unshuffled')
def unshuffled():
    newDeck = createDeck()
    return jsonify(newDeck)

@app.route('/unshuffled/jokers')
def unshuffledJokers():
    newDeck = createDeck()
    newDeck.append(["Joker", "Joker"])
    newDeck.append(["Joker", "Joker"])
    return jsonify(newDeck)


if __name__ == '__main__':
    app.run(debug=True)