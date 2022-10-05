# Here is the full War game with comments
from random import shuffle                                              # from the random module, import the shuffle function


class Card:                                                             # Create the Card class
    suits = ["spades", "hearts", "diamonds", "clubs"]                   # Create a list of suits, suits are arranged in order of strength
    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9",        # Create a list of values, none is used twice so indexes match values
              "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):                                    # Initiate the class with two parameters
        """suit and value should be integers"""
        self.value = value
        self.suit = suit

    def __lt__(self, other):                                            # The definitions in the magic methos allow us to compare two card objects in an expression
        if self.value < other.value:                                    # using the less than operators
            return True
        if self.value == other.value:
            if self.suit < other.suit:                                  # If the value is the same, the value of the suit is the icebreaker.
                return True
            else:
                return False
        return False

    def __gt__(self, other):                                            # The definitions in the magic methos allow us to compare two card objects in an expression
        if self.value > other.value:                                    # using the greater than operators
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):                                                 # Use the value and suit instance to look up and print the card a Card object represents
        return self.values[self.value] + " of " + self.suits[self.suit]


class Deck:                                                             # Define a class to represent the deck
    def __init__(self):
        self.cards = []
        for i in range(2, 15):                                          # The two for-loops in __init__ create Card objects for all 52 cards
            for j in range(4):
                self.cards.append(Card(i, j))                           # Append combination to cards list
        shuffle(self.cards)                                             # Shuffle function used to make the deck order random

    def remove_card(self):                                              # Method that removes and returns a card from the cards list.
        if len(self.cards) == 0:
            return                                                      # Returns None if it is empty
        return self.cards.pop()                                         # Else remove item from list


class Player:                                                           #  Need a class to represent each player in the game, 3 variables
    def __init__(self, name):
        self.wins = 0                                                   # Keep track of how many rounds each player has won
        self.card = None                                                # Represent the card each player is holding
        self.name = name                                                # Keep track of the player's name


class Game:                                                             # You need a class to represent the game
    def __init__(self):                                                 # Create game class
        name1 = input("player1 name ")
        name2 = input("player2 name ")
        self.deck = Deck()                                              # Create a new deck object and store it
        self.player1 = Player(name1)                                    # Create a player1 name object and store it
        self.player2 = Player(name2)

    def play_game(self):                                                # Start the game
        cards = self.deck.cards
        print("beginning War!")
        response = None                                                 # Assign the variable response to the input of the user
        while len(cards) >= 2:
            response = input('q to quit. Any other key to play.')       # Keep the game going until 2 cards are left
            if response == 'q':
                break
            player1_card = self.deck.remove_card()                      # Assign card to player 1
            player2_card = self.deck.remove_card()                      # Assign card to player 2
            print("{} drew {} {} drew {}".format(self.player1.name, player1_card, self.player2.name, player2_card))
            if player1_card > player2_card:                             # Compare both cards
                self.player1.wins += 1                                  # Increment player1's wins
                print("{} wins this round".format(self.player1.name))
            else:
                self.player2.wins += 1
                print("{} wins this round".format(self.player2.name))
        print("The War is over.{} wins".format(self.winner(self.player1, self.player2))) # End of game

    def winner(self, player1, player2):                                 # Create a winner method
        if player1.wins > player2.wins:                                 # Compare number of rounds won
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "It was a tie!"                                          # else, tie

game = Game()
game.play_game()