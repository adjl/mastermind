class Board(object):
    def __init__(self, length, width, turns):
        self.length = length
        self.width = width

        self.board = []

        board_row = self.make_row()
        board_end = self.make_row("+", "-")

        self.board.append(board_end)
        for row in range(turns * 2 + 1):
            self.board.append(board_row)
        self.board.append(board_end)


    def make_row(self, border="|", slot=" "):
        return (" " * (self.width / 4)) + border + \
                (slot * (self.length * 3 + 2)) + border + \
                (slot * (self.length * 2 + 1)) + border


    def display(self):
        print '\n'.join(self.board) + '\n'


    def update(self, turn, guess, feedback):
        board_row = (" " * (self.width / 4)) + "|  "

        for colour in guess:
            board_row += colour + "  "

        board_row += "| "

        for key in feedback:
            board_row += key + " "

        for empty_key in range(self.length - len(feedback)):
            board_row += "  "

        board_row += "|"

        self.board[(turn + 1) * 2] = board_row
