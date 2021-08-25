from flask import Flask, request, jsonify
import random

app = Flask(__name__)

#lists containing card data
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Clubs", "Spades", "Diamonds"]


def createDeck (count):
    newDeck = []
    for value in values:
        for suit in suits:
            newCard =[]
            newCard.append(value)
            newCard.append(suit)
            i = 0
            while i < count:
                newDeck.append(newCard)
                i += 1
    return newDeck


@app.route("/")
def test ():
    return "Basic Functionality Running"

@app.route('/deck')
@app.route('/deck/<int:count>')
def deck(count = 1):
    newDeck = createDeck(count)
    random.shuffle(newDeck)
    return jsonify(newDeck)

@app.route('/deck/jokers')
# @app.route('/deck/jokers/<int:count>')
def jokerDeck(count = 1):
    newDeck = createDeck(count)
    random.shuffle(newDeck)
    newDeck.insert(random.randint(0, len(newDeck)),["Joker", "Joker"])
    newDeck.insert(random.randint(0, len(newDeck)),["Joker", "Joker"])
    return jsonify(newDeck)

@app.route('/unshuffled')
@app.route('/unshuffled/<int:count>')
def unshuffled(count = 1):
    newDeck = createDeck(count)
    return jsonify(newDeck)

@app.route('/unshuffled/jokers')
# @app.route('/unshuffled/jokers/<int:count>/')
def unshuffledJokers(count = 1):
    newDeck = createDeck(count)
    newDeck.append(["Joker", "Joker"])
    newDeck.append(["Joker", "Joker"])
    return jsonify(newDeck)


if __name__ == '__main__':
    app.run(debug=True)