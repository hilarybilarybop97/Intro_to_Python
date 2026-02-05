import random

class Card:
    VALUES = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
              '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 
              'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def value(self, rank):
        return Card.VALUES[rank]

class Deck:
    SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        self.deck = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        return f"{self.deck}"

    def __repr__(self):
        return f"{self.deck}"
        
class Participant:
    def __init__(self):
        self.hand = []

    def hit(self, deck):
        self.hand.append(deck.deal())

    def stay(self):
        #STUB
        pass

    def is_busted(self):
        if self.score() > 21:
            return True
        
        return False

    def score(self):
        values = [card.value(card.rank) for card in self.hand]
        if sum(values) > 21 and 11 in values:
            return sum(values) - 10
        return sum(values)

class Player(Participant):
    def __init__(self):
        super().__init__()
        #STUB
        #score? hand? money available?
        self.balance = 5

class Dealer(Participant):
    def __init__(self):
        super().__init__()

    def hit(self, deck):
        super().hit(deck)

    def stay(self):
        #STUB
        pass

    def hide(self):
        return ["Hidden"] + self.hand[1:]

    def reveal(self):
        print()
        print("Dealer's Cards: ")
        for card in self.hand:
            print(card)

class TwentyOneGame:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()

    def start(self):
        #SPIKE
        self.display_welcome_message()
        self.deal_cards()
        self.show_cards()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        for _ in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)

    def show_cards(self):
        print()
        print("Dealer's Hand:")
        for card in self.dealer.hide():
            print(card)
        print()
        print("Player's Hand:")
        for card in self.player.hand:
            print(card)
        
    def player_turn(self):
        print()
        print("Player goes first:")
        while True:
            choice = input("Would you like to hit ('h') or stay ('s')? ")
            if choice not in ['h', 's']:
                print("Invalid input.  Enter only 'h' or 's'. ")
                continue

            if choice == 'h':
                self.player.hit(self.deck)
                print("You chose to hit!")
                self.show_cards()
                print(f"Your score is: {self.player.score()}")
                #add score

            if choice == 's' or self.player.is_busted(): #add busted
                self.player.stay()
                print()
                print("You chose to stay!")
                break

        if self.player.is_busted():
            print()
            print("Sorry! You've busted!")
            self.dealer.reveal()
            print()
            print("Dealer wins!")
            

    def dealer_turn(self):
    #STUB
        #STUB
        pass

    def display_welcome_message(self):
        print("Welcome to Twenty-One!")
        print()
        print("The player whose hand comes closest to 21 points in value wins the hand.")
        print()
        print("Each player begins with $5 to bet with.")
        print("Each hand is worth $1.")

    def display_goodbye_message(self):
        print()
        print("Thank you for playing Twenty-One!")

    def display_result(self):
        #STUB
        pass

game = TwentyOneGame()
game.start()