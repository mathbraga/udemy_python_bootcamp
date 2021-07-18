import random

suits = ("Hearts", "Spades", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",\
    "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,\
    "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12,\
    "King": 13, "Ace": 14}

def check_winner(p1, p2):
    if len(p1.all_cards) == len(p2.all_cards) == 0:
        return [True, 0]
    elif len(p1.all_cards) == 0:
        return [True, 2]
    elif len(p2.all_cards) == 0:
        return [True, 1]
    else:
        return [False, None]

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def remove_card(self):
        return self.all_cards.pop(0)

player_1 = Player("Albert")
player_2 = Player("Samantha")

new_deck = Deck()
new_deck.shuffle()
for i in range(26):
    player_1.add_cards(new_deck.deal_one())
    player_2.add_cards(new_deck.deal_one())

is_game_active = True
is_war = False
pile = []
round = 0

while is_game_active:
    p1_card = player_1.remove_card()
    p2_card = player_2.remove_card()
    print(f"{len(player_1.all_cards)}\t{len(player_2.all_cards)}")

    if p1_card.value > p2_card.value:
        player_1.add_cards([p1_card, p2_card] + pile)
        pile = []
        is_war = False
    elif p2_card.value > p1_card.value:
        player_2.add_cards([p1_card, p2_card] + pile)
        pile = []
        is_war = False
    else:
        is_war = True
    
    if is_war:
        pile += [p1_card, p2_card]
        if len(player_1.all_cards) < 5 and len(player_2.all_cards) < 5:
            print("Game is a tie.")
            is_game_active = False
            break
        elif len(player_1.all_cards) < 5:
            print(f"{player_2.name} has won.")
            is_game_active = False
            break
        elif len(player_2.all_cards) < 5:
            print(f"{player_1.name} has won.")
            is_game_active = False
            break
        else:
            for i in range(5):
                pile += [player_1.remove_card(), player_2.remove_card()]
            is_war = False

    if check_winner(player_1, player_2)[0]:
        if check_winner(player_1, player_2)[1] == 0:
            print("Game is a tie.")
            is_game_active = False
        else:
            print(f"{[player_1.name, player_2.name][check_winner(player_1, player_2)[1]-1]} has won.")
            is_game_active = False