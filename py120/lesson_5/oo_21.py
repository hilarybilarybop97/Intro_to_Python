import random
import os
import time

def clear_screen():
    os.system('clear')

class Card:
    SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King', 'Ace')
    VALUES = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
              '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 
              'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, rank, suit):
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def value(self):
        return Card.VALUES[self.rank]

class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for rank in Card.RANKS
                                      for suit in Card.SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        return f"{self.deck}"

    def __repr__(self):
        return f"{self.deck}"

    def reshuffle(self):
        self.deck = [Card(rank, suit) for rank in Card.RANKS
                                      for suit in Card.SUITS]
        self.shuffle()

class Participant:
    def __init__(self):
        self.hand = []

    def hit(self, deck):
        self.hand.append(deck.deal())

    def stay(self):
        pass

    def is_busted(self):
        if self.score() > TwentyOneGame.TARGET_SCORE:
            return True

        return False

    def new_hand(self):
        self.hand = []

    def score(self):
        total = 0
        aces = 0

        for card in self.hand:
            total += card.value()
            if card.rank == 'Ace':
                aces += 1

        while total > TwentyOneGame.TARGET_SCORE and aces:
            total -= 10
            aces -= 1

        return total

class Player(Participant):
    def __init__(self):
        super().__init__()

class Dealer(Participant):
    def __init__(self):
        super().__init__()

    def hide(self):
        return ["???????"] + [str(card) for card in self.hand[1:]]

    def reveal(self):
        print()
        print("Dealer's Hand: ")
        for card in self.hand:
            print(f"==> {card}")

        print()
        print(f"Dealer's score: {self.score()}")
        print()

class Wager:
    BROKE = 0
    RICH = 10
    INITIAL_WAGER = 5

    def __init__(self):
        self.balance = Wager.INITIAL_WAGER

    def __str__(self):
        return f"${self.balance}"

    def __repr__(self):
        return f"${self.balance}"

    def update(self, result):
        if result == 'win':
            self.balance += 1
        elif result == 'loss':
            self.balance -= 1
        else:
            pass

    def is_broke(self):
        return self.balance == Wager.BROKE

    def is_rich(self):
        return self.balance == Wager.RICH

    def display(self):
        print(f"Current balance is: {self}")

class TwentyOneGame:
    TARGET_SCORE = 21
    DEALER_STAY = TARGET_SCORE - 4

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()
        self.balance = Wager()

    def start(self):
        self.display_welcome_message()

        while True:
            self.deal_cards()
            self.show_cards()
            self.player_turn()
            clear_screen()
            self.dealer_turn()
            self.display_result()
            self.balance.update(self.result())
            self.balance.display()
            if self.balance.is_broke():
                print("You're broke! Game Over.")
                break
            if self.balance.is_rich():
                print("You're rich and the house always wins! Game Over.")
                break
            if not self.play_again():
                break
            self.player.new_hand()
            self.dealer.new_hand()
            self.deck.reshuffle()

        self.display_goodbye_message()

    def deal_cards(self):
        for _ in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)

    def show_cards(self, hide=True):
        print()
        print("Dealer's Hand:")

        if hide:
            for card in self.dealer.hide():
                print(f'==> {card}')

        if not hide:
            for card in self.dealer.hand:
                print(f'==> {card}')

        print()
        print("Player's Hand:")
        for card in self.player.hand:
            print(f'==> {card}')
        print()
        print(f"Player's score: {self.player.score()}")

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

            if choice == 's' or self.player.is_busted():
                self.player.stay()
                break

        if choice == 's':
            print()
            print("You chose to stay!")

        if self.player.is_busted():
            print()
            print("Sorry! You've busted!")
            print()

    def dealer_turn(self):
        if self.player.is_busted():
            self.dealer.reveal()
            return

        print()
        print("Dealer's turn...")
        time.sleep(1)
        self.dealer.reveal()

        while self.dealer.score() < TwentyOneGame.DEALER_STAY:
            print("Dealer hits!")
            self.dealer.hit(self.deck)
            self.dealer.reveal()

        if self.dealer.is_busted():
            self.show_cards(hide=False)

        else:
            print(f"Dealer stays at {self.dealer.score()}.")
            self.show_cards(hide=False)

    def display_welcome_message(self):
        print("Welcome to Twenty-One!")
        print()
        print("The player whose hand comes closest to 21"
               "points in value wins the hand.")
        print()
        print(f"Each player begins with ${Wager.INITIAL_WAGER} to bet with."
               "Each wager is worth $1.")

    def display_goodbye_message(self):
        print()
        print("Thank you for playing Twenty-One!")
        print("Goodbye!")

    def find_winner(self):
        if self.player.is_busted():
            return self.dealer
        if self.dealer.is_busted():
            return self.player
        if self.player.score() > self.dealer.score():
            return self.player
        if self.dealer.score() > self.player.score():
            return self.dealer

        return "tie"

    def result(self):
        game_result = self.find_winner()

        if game_result == self.dealer:
            return 'loss'
        if game_result == self.player:
            return 'win'

        return 'tie'

    def display_result(self):
        if self.find_winner() == self.dealer:
            print("Dealer wins!")
        elif self.find_winner() == self.player:
            print("You win!")
        else:
            print("It's a tie!")

    def play_again(self):
        while True:
            print()
            choice = input("Keep playing? (y/n) ")
            if choice in ['y', 'n']:
                break
            print("Enter only 'y' or 'n'. ")

        return choice == 'y'

game = TwentyOneGame()
game.start()