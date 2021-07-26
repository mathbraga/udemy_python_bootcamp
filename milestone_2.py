import random

suits = ("Hearts", "Spades", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",\
    "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,\
    "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10,\
    "King": 10, "Ace": 11}

class Card():
    def __init__(self, rank, suit, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit} {self.value}"


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit, values[rank]))

class Dealer():

    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.power = 0

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()

    def add_hand(self, card):
        self.hand.append(card)
        self.power += card.value

    def clear_hand(self):
        self.hand = []
        self.power = 0

    def reset_deck(self, pile):
        self.deck += pile


class Player():
    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)
        self.hand = []
        self.power = 0
    
    add_hand = Dealer.add_hand

    clear_hand = Dealer.clear_hand

    def bet(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

game_deck = Deck()
dealer = Dealer(game_deck.deck)
dealer.shuffle()

game_is_active = False
round_is_active = False
player_bid = 0

print("Welcome to BlackJack!")
answer = input("Do you wish to play? (y|n) ").lower()
if answer == "y":
    game_is_active = True
    p_name = input("Type in your name: ")
    p_balance = input("Type in your balance: ")
    player = Player(p_name, p_balance)
else:
    game_is_active = False

while game_is_active:
    print("What do you wish to do?")
    print("1 - Bet")
    print("2 - Increase my balance")
    print("3 - Exit")
    option = int(input("Your choice: "))
    if option == 1:
        player_bet = int(input("What is your bet: "))
        if player.bet(player_bet):
            print("Your balance now is", player.balance)
            round_is_active = True

    elif option == 2:
        player.balance += int(input("Insert value to add: "))
        print("Your current balance is:", player.balance)

    elif option == 3:
        print("Thank you for playing.")
        game_is_active = False

    while round_is_active:
        print("Round start.")
        print("Your bet is", player_bet)
        print("Dealer deals the cards")

        player.add_hand(dealer.deal_one())
        d_facedown = dealer.deal_one()
        player.add_hand(dealer.deal_one())
        dealer.add_hand(dealer.deal_one())

        print("Your hand is:")
        for card in player.hand:
            print(card)
        print("Power:", player.power)
        print("-------------------")

        print("Dealer hand is:")
        for card in dealer.hand:
            print(card)
        print("Power:", dealer.power)
        print("-------------------")

        round_is_active = False