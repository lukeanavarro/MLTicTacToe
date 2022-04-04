class TicTacToe:
    def __init__(self):
        self.board = " " * 9
        self.turn = "X"
        self.log = []

    def __repr__(self):
        return f"{self.board[0]}|{self.board[1]}|{self.board[2]}\n" \
               f"_____\n" \
               f"{self.board[3]}|{self.board[4]}|{self.board[5]}\n" \
               f"_____\n" \
               f"{self.board[6]}|{self.board[7]}|{self.board[8]}\n"

    def __str__(self):
        return self.__repr__()

    def change_turn(self):
        self.turn = "O" if self.turn == "X" else "X"

    def print_board(self):
        return f"{self.board[0]}|{self.board[1]}|{self.board[2]}\n" \
               f"_____\n" \
               f"{self.board[3]}|{self.board[4]}|{self.board[5]}\n" \
               f"_____\n" \
               f"{self.board[6]}|{self.board[7]}|{self.board[8]}\n"

    def get_turn(self):
        return self.turn

    def move(self, n):
        """
        Make a move at space n if legal, updates self.board
        Args:
            n: int 0-8

        Returns: -1 if move illegal else none
        """

        if self.board[n] == ' ' and n < 9:
            self.board = self.board[0:n] + self.turn + self.board[n+1:]
        else:
            print("Illegal Move, Try Again")

    def record_move(self):
        self.log.append(self.board[:])

    def get_log(self):
        return self.log

    def victory_check(self):
        victory = f"{self.turn}{self.turn}{self.turn}"
        if self.board[0:3] or self.board[3:6] or self.board[6:] or self.board[0::3] or self.board[1::3] or \
                self.board[2::3] or self.board[0::4] or self.board[2:7:2] == victory:
            return True, self.turn
        elif " " not in self.board:
            return True, "Cats"

    def game(self):
        while True:
            print(self.print_board())
            space = input("Make a move (0-8): ")
            self.move(int(space))
            victory, turn = self.victory_check()
            if victory and turn == "Cats":
                print("Cats Game")
                break
            elif victory:
                print(f"{turn} Wins!")
                break
            self.change_turn()




