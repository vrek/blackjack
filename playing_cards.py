"""A series of classes to work with playing cards"""
import random
class PlayingCard(object):
    """Class to handle individual playing cards
    inputs are suit and value, all lower case"""
    def __init__(self, suit, face_value):
        suits = ('hearts', 'diamonds', 'spades', 'clubs')
        face_values = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen', 'king', 'ace')
        if suit in suits:
            self.suit = suit
        else:
            raise TypeError
        if face_value in face_values:
            self.face_value = face_value
        else:
            raise TypeError    
    def show(self):
        """function to show the value of a playing card"""
        print(f"{self.face_value} of {self.suit}")
class Deck:
    """Class to hold and store a deck of cards"""
    suits = ('hearts', 'diamonds', 'spades', 'clubs')
    face_values = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen', 'king', 'ace')
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        """function to build a deck"""
        for s in self.suits:
            for v in self.face_values:
                self.cards.append(PlayingCard(s,v))
    def shuffle(self):
        """function to shuffle a deck"""
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):
        """function to draw a card"""
        return self.cards.pop()
    def show(self):
        """function to display a hand"""
        for c in self.cards:
            c.show()
class Player:
    """Class to hold an instance of a player"""
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.wins = 0
    def draw(self, deck):
        """Function to draw a card"""
        self.hand.append(deck.drawCard())
        return self
    def showHand(self):
        """Function to show their hand"""
        for card in self.hand:
            card.show()
    def foldHand(self):
        """Function to fold their hand"""
        self.hand.clear()
