class Board(object):
    def __init__(self, pattern_length, screen_width, turns):
        self.pattern_length = pattern_length
        self.screen_width = screen_width

        self.board = []
        board_row = self.create_row("|", " ")
        board_end = self.create_row("+", "-")

        self.board.append(board_end)
        for row in range(turns * 2 + 1):
            self.board.append(board_row)
        self.board.append(board_end)


    def create_row(self, border, slot):
        return (" " * (self.screen_width / 4)) + border + \
                (slot * (self.pattern_length * 3 + 2)) + border + \
                (slot * (self.pattern_length * 2 + 1)) + border


    def display(self):
        print '\n'.join(self.board) + '\n'


    def update(self, turn, guess, feedback):
        board_row = (" " * (self.screen_width / 4)) + "|  "

        for colour in guess:
            board_row += colour + "  "

        board_row += "| "

        for key in feedback:
            board_row += key + " "
        for empty_key in range(self.pattern_length - len(feedback)):
            board_row += "  "

        board_row += "|"

        self.board[(turn + 1) * 2] = board_row
