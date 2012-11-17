import random
import sys
import time

from player import Player
from solving_algorithm import generate_solutions

class ComputerPlayer(Player):
    def __init__(self):
        super(ComputerPlayer, self).__init__()

        self.PAUSE = 0.1
        self.names = ['Chell', 'GLaDOS', 'Curiosity Core', 'Turret', 'Companion Cube', 'Wheatley', 'Cave Johnson', 'Caroline', 'Cake']


    def __type(self, message):
        sys.stdout.write(' ')
        sys.stdout.flush()
        time.sleep(self.PAUSE * 5)

        for character in message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(self.PAUSE)

        time.sleep(self.PAUSE * 5)
        print


    def remember_rules(self, pattern_length, pattern_colours):
        self.pattern_length = pattern_length
        self.pattern_colours = pattern_colours

    
    def ready_for_game(self):
        self.solutions = []
        self.colours_tried = 0
        self.solving_phase = '1'


    def ask_for_name(self, message=''):
        self.name = random.choice(self.names)

        if message:
            print message.rstrip(),
        self.__type(self.name)


    def choose_secret_pattern(self, message=''):
        self.secret_pattern = []

        for colour in range(self.pattern_length):
            self.secret_pattern.append(random.choice(self.pattern_colours))

        if message:
            print message.rstrip(),
        self.__type("?" * self.pattern_length)


    def make_guess(self, message='', allow_save=False):
        self.guess = []

        if self.solving_phase == '1':
            colour = list(self.pattern_colours).pop(self.colours_tried)
            for peg in range(self.pattern_length):
                self.guess.append(colour)

        elif self.solving_phase == '2':
            for colour in self.solutions:
                self.guess.append(colour)

        elif self.solving_phase == '3':
            solution = self.solutions.pop()
            for colour in solution:
                self.guess.append(colour)

        if message:
            print message.rstrip(),
        self.__type(''.join(self.guess))


    def analyse_feedback(self, feedback):
        if self.solving_phase == '1':
            colour = self.guess[0]
            for key in feedback:
                self.solutions.append(colour)
            self.colours_tried += 1

            if self.colours_tried == len(self.pattern_colours) - 1:
                colour = list(self.pattern_colours).pop(self.colours_tried)
                for peg in range(self.pattern_length - len(self.solutions)):
                    self.solutions.append(colour)
                self.colours_tried += 1

            if len(self.solutions) == self.pattern_length:
                self.solving_phase = '2'

        elif self.solving_phase == '2':
            self.solutions = generate_solutions(self.guess, feedback)
            self.solving_phase = '3'

        elif self.solving_phase == '3':
            new_solutions = generate_solutions(self.guess, feedback)

            current_solutions = set(map(tuple, self.solutions))
            new_solutions = set(map(tuple, new_solutions))

            solutions = current_solutions & new_solutions
            solutions = map(list, list(solutions))

            self.solutions = solutions
