from enum import Enum, auto
from typing import List

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Rank(Enum):
    ACE = "Ace"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"

class Card:

    def __init__(self, rank, suit):

        # if invalid input
        if not isinstance(rank, Rank):
            raise ValueError(f"Invalid rank: {rank}")
        if not isinstance(suit, Suit):
            raise ValueError(f"Invalid suit: {suit}")
        
        self.rank = rank
        self.suit = suit

    # print the card's value
    # equal to overriding the print function
    def __str__(self):
        return f"{self.rank.value} of {self.suit.value}"
    
    def __repr__(self):
        return f"Card(rank={self.rank}, suit={self.suit})"
    
class Deck:
    def __init__(self):
        self.cards = set()  #init empty set
        
    def populate(self):
        for rank in Rank:
            for suit in Suit:
                card = Card(rank, suit)
                self.cards.add(card)



class Player:

    def __init__(self, name, hand=None):
        self.name = name
        self.hand = hand if hand is not None else[]

    # override print fn
    def __str__(self):
        return f"Player(name={self.name}, hand={self.hand})"
    
    # What does __repr__ do exactly?
    def __repr__(self):
        return self.__str__()
    

    # draw cards from deck
    def draw_card(self, deck, card):
        

    # 
    def play_card(hand):
        # if the player has 


    def ask_for_card(self):


    def has_card(self, other_player):
        # return true if this player has the cards of a rank that the other player has for
        for rank in Rank:
            if self.hand.card(rank) == 


    def get_card(self, player):
        # if has_card() returns true, moves player2's cards of requested to player2's hand
