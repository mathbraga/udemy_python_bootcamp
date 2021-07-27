from milestone_2_warmup import check_winner
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
        if self.power > 21:
            self.power = 0
            for c in self.hand:
                if c.rank == "Ace":
                    c.value = 1
                self.power += c.value

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
round_count = 0

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
    print("1 - Show balance")
    print("2 - Bet")
    print("3 - Increase my balance")
    print("4 - Exit")
    option = int(input("Your choice: "))

    if option == 1:
        print("Your balance is ", player.balance)
        continue

    elif option == 2:
        player_bet = int(input("What is your bet: "))
        if player.bet(player_bet):
            print("Your balance now is", player.balance)
            round_is_active = True

    elif option == 3:
        player.balance += int(input("Insert value to add: "))
        print("Your current balance is:", player.balance)
        continue

    elif option == 4:
        print("Thank you for playing.")
        game_is_active = False
        break

    
    print("Round start.")
    print("Your bet is", player_bet)
    print("Dealer deals the cards")

    player.add_hand(dealer.deal_one())
    d_facedown = dealer.deal_one()
    player.add_hand(dealer.deal_one())
    dealer.add_hand(dealer.deal_one())

    while round_is_active:
        round_count += 1

        print("Your hand is:")
        for card in player.hand:
            print(card)
        print("Power:", player.power)
        print("-------------------")

        print("Dealer hand is:")
        for card in dealer.hand:
            print(card)
        if round_count == 1:
            print("And a facedown card.")
        print("Power:", dealer.power)
        print("-------------------")

        if player.power == 21 and round_count == 1:
            dealer.add_hand(d_facedown)
            print("Dealer facedown card is:", d_facedown)
            print("Dealer power is:", dealer.power)
            print("-------------------")
            if dealer.power == 21:
                print("It's a BlackJack tie.")
                print("Bet will be refounded.")
                player.balance += player_bet
            else:
                print("BlackJack! Congratulations.")
                print("You win 2x your bet:", player_bet*2)
                player.balance += player_bet*2

            dealer.reset_deck(player.hand + dealer.hand)
            player.clear_hand()
            dealer.clear_hand()
            round_is_active = False
            break
        elif player.power == 21:
            pass

        print("What do you wish to do?")
        print("1 - Hit")
        print("2 - Stand")
        option = int(input("Your choice: "))

        if option == 1:
            player.add_hand(dealer.deal_one())
        elif option == 2:
            print("Stand")
