from typing import Text
from app import db

class Deck(db.Model):
    __tablename__='decks'
    id = db.Column(db.Integer, primary_key=True)
    deck = db.column(db.ARRAY(Text))

    def __init__(self, id, deck):
        self.id = id
        self.deck = deck

    def __repr__(self):
        return'<id {}>'.format(self.id)

    def serialize(self):
        return{
            'id': self.id,
            'deck': self.deck
        }