import random

suits = ('♥', '♦', '♠', '⯁')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __repr__(self):
        return f'┌─────────┐\n|{self.rank}        |\n│         │\n|    {self.suit}    |\n' \
               f'│         │\n|        {self.rank}|\n└─────────┘\n'


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def take_card(self):
        return self.cards.pop()


deck = Deck()
deck.shuffle()

player1 = Player(input("Enter player 1 name: "))
player2 = Player(input("Enter player 2 name: "))

player1.cards = deck.all_cards[:26]
player2.cards = deck.all_cards[26:]

winner = ""
cards_on_table = []
counter = 1

while True:
    print(counter)
    counter += 1

    print(f'{player1.name} has {len(player1.cards)} cards')
    print(f'{player2.name} has {len(player2.cards)} cards')

    player1_card = ""
    player2_card = ""

    if len(player1.cards) > 0:
        player1_card = player1.take_card()
        cards_on_table.append(player1_card)
    else:
        winner = player2
        break
    if len(player2.cards) > 0:
        player2_card = player2.take_card()
        cards_on_table.append(player2_card)
    else:
        winner = player1
        break
    if player1_card.value > player2_card.value:
        player1.cards += cards_on_table
        cards_on_table = []
        print(f'{player1.name} win the round')
        continue
    if player1_card.value < player2_card.value:
        player2.cards += cards_on_table
        cards_on_table = []
        print(f'{player2.name} win the round')
        continue
    # in case of war
    print("War")
    if len(player1.cards) > 3:
        for _ in range(3):
            cards_on_table.append(player1.take_card())
    else:
        winner = player2
        break
    if len(player2.cards) > 3:
        for _ in range(3):
            cards_on_table.append(player2.take_card())
    else:
        winner = player1
        break

if winner == player1:
    print(f'The winner is {player1.name}')
else:
    print(f'The winner is {player2.name}')
