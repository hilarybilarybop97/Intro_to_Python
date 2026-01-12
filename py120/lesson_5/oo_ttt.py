class Square:
    def __init__(self):
        #STUB
        pass

class Board:
    def __init__(self):
        #STUB
        pass    
    
    def display(self):
        print()
        print("     |     |")
        print("  O  |     |  O")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print("     |  X  |")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print("  X  |     |")
        print("     |     |")
        print()

class Row:
    def __init__(self):
        #STUB
        pass

class Marker:
    def __init__(self):
        #STUB
        pass

class Player:
    def __init__(self):
        #STUB
        pass
    
    def mark(self):
        #STUB
        pass

    def play(self):
        #STUB
        pass

class Human(Player):
    def __init__(self):
        #STUB
        pass

class Computer(Player):
    def __init__(self):
        #STUB
        pass

class TTTGame:
    def __init__(self):
        self.board = Board()

    def play(self):
        #SPIKE
        self.display_welcome_message()

        while True:
            self.board.display()

            self.first_player_moves()
            if self.is_game_over():
                break

            self.second_player_moves()
            if self.is_game_over():
                break

            break #execute loop once for now
        
        self.board.display()
        self.display_results()
        self.display_goodbye_message()
    
    def display_welcome_message(self):
        print('Welcome to Tic Tac Toe!')

    def display_goodbye_message(self):
        print('Thanks for playing Tic Tac Toe! Goodbye!')

    def display_results(self):
        #STUB
        pass

    def first_player_moves(self):
        #STUB
        pass

    def second_player_moves(self):
        #STUB
        pass
    
    def is_game_over(self):
        #STUB
        return False

game = TTTGame()
game.play()

