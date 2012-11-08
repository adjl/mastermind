class Board(object):
    def __init__(self, turns, length, width):
        self.board = []

        board_end = (" " * (width / 4)) + "+" + ("-" * (length * 3 + 2)) + "+" + ("-" * (length * 2 + 1)) + "+"
        board_row = (" " * (width / 4)) + "|" + (" " * (length * 3 + 2)) + "|" + (" " * (length * 2 + 1)) + "|"

        self.board.append(board_end)
        for row in range(turns * 2 + 1):
            self.board.append(board_row)
        self.board.append(board_end)


    def display(self):
        print '\n'.join(self.board) + '\n'


    def update(self, game, guess, feedback, length, width):
        board_row = (" " * (width / 4)) + "|  "

        for colour in guess:
            board_row += colour + "  "

        board_row += "| "

        for key in feedback:
            board_row += key + " "

        for empty_key in range(length - len(feedback)):
            board_row += "  "

        board_row += "|"

        self.board[(game + 1) * 2] = board_row
