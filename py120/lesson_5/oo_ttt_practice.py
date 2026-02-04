import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_unused_square(self, key):
        return self.squares[key].is_unused()

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)
    
    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class Score:
    def __init__(self):
        self.score = {'wins':   0,
                      'losses': 0,
                      'ties':   0,
                      }

    def reset(self):
        pass

    def get_values(self):
        values = list(self.score.values())
        return values[:-1]

    def __str__(self):
        return f"Current Score: {self.score}"

    def update(self, player):
        if player == 'human':
            self.score['wins'] += 1
        elif player == 'computer':
            self.score['losses'] += 1
        else:
            self.score['ties'] += 1

    def display(self):
        print(self)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.score = Score()

    def play(self):
        self.display_welcome_message()

        while True:
            self.play_one_round()
            if self.play_again() == 'n':
                break

        self.display_goodbye_message()

    def match_play(self):
        self.display_welcome_message()

        while True:
            self.play_one_round()

            if 3 in self.score.get_values():
                self.display_match_results()
                self.display_goodbye_message()
                break
        
            if self.play_again() == 'n':
                self.score.display()
                break
        
    def play_one_round(self):
        self.board.reset()
        self.board.display_with_clear()
        self.score.display()

        while True:
            self.human_moves()
            if self.is_game_over():
                break

            self.computer_moves()
            if self.is_game_over():
                break

            self.board.display_with_clear()

        self.board.display_with_clear()
        self.display_results()
        self.score.update(self.winner())
        self.score.display()

    def display_welcome_message(self):
        clear_screen()
        print('Welcome to Tic Tac Toe!')
        print('The first player to 3 wins the match!')
        print()

    def display_goodbye_message(self):
        print('Thanks for playing Tic Tac Toe! Goodbye!')

    def winner(self):
        if self.is_winner(self.human):
            return 'human'
        elif self.is_winner(self.computer):
            return 'computer'
        else:
            return 'tie'

    def display_match_results(self):
        if self.score.get_values()[0] == 3:
            print('Congrats, human! You were first to 3!')
        elif self.score.get_values()[1] == 3:
            print('Better luck next time, human! Computer was first to 3!')

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game.  How boring.")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False
    
    @staticmethod
    def _join_or(choices, punctuation=', ', conjunction='or'):
        str_choices = [str(choice) for choice in choices]

        if len(str_choices) == 1:
            return str_choices[0]
        if len(str_choices) == 2:
            return f"{str_choices[0]} {conjunction} {str_choices[1]}"

        last = str_choices[-1]
        initial = str_choices[:-1]
        return punctuation.join(initial) + punctuation + conjunction + ' ' + last

    def human_moves(self):
        while True:
            valid_choices = self.board.unused_squares()
            printable_choices = TTTGame._join_or(valid_choices)
            prompt = f"Choose a square ({printable_choices}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = self.offensive_computer_move()

        if not choice:
            choice = self.defensive_computer_move()

        if not choice:
            choice = self.pick_center_square()

        if not choice:
            choice = self.pick_random_square()

        self.board.mark_square_at(choice, self.computer.marker)
    
    def pick_center_square(self):
        return 5 if self.board.is_unused_square(5) else None

    def pick_random_square(self):
        valid_choices = self.board.unused_squares()
        return random.choice(valid_choices)

    def find_critical_square(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            key = self.critical_square(row, player)
            if key:
                return key

        return None

    def offensive_computer_move(self):
        return self.find_critical_square(self.computer)

    def defensive_computer_move(self):
        return self.find_critical_square(self.human)

    def critical_square(self, row, player):
        if self.board.count_markers_for(player, row) == 2:
            for key in row:
                if self.board.is_unused_square(key):
                    return key

        return None

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def play_again(self):
        answer = input("Play again? Enter 'y' or 'n' ")
        while True:
            valid_answers = ('y', 'n')
            if answer.casefold() in valid_answers:
                return answer.casefold()
            answer = input("Invalid answer. Enter only 'y' or 'n' ")

game = TTTGame()
game.match_play()