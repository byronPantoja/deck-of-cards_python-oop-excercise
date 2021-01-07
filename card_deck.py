class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


print(Card("A", "Clubs"))


class Deck:
    def __init__(self):
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

        print(self.cards)


Deck()
