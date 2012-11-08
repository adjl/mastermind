import os
import pickle
import random
import sys
import time

from functions import is_odd

class Game(object):
    def __init__(self):
        self.PAUSE = 2
        self.WIDTH = 80

        self.MIN = 3
        self.MAX = 8

        self.SAVE_DIR = 'saves'

        self.modes = ['s', 'm', 'd', 'c', 'i', 'o', 'q']
        self.settings = {'g': 'games', 'p': 'pegs', 'c': 'colours', 'b': None}

        self.colour_codes = ['r', 'g', 'b', 'c', 'm', 'y', 'o', 'p']
        self.feedback_keys = {'correct': 'b', 'partially_correct': 'w'}

        self.colour_names = {'r': 'red', 'g': 'green', 'b': 'blue', 'c': 'cyan', 'm': 'magenta', 'y': 'yellow', 'o': 'orange', 'p': 'purple'}
        self.feedback_names = {'b': 'black', 'w': 'white'}

        self.games = 2
        self.pegs = 4
        self.colours = 6
        self.turns = 12

        self.guesses = {}
        self.feedback = {}


    def __clear(self):
        os.system('clear')


    def __pause(self, pause):
        time.sleep(pause)


    def menu(self):
        while True:
            self.__clear()

            print "Mastermind"
            print "-" * self.WIDTH
            print "[S] Single-player (PvC)"
            print "[M] Multiplayer (PvP)"
            print "[D] Duel (CvC)"
            print "[C] Continue"
            print "[I] Instructions"
            print "[O] Options"
            print "[Q] Quit"
            print "-" * self.WIDTH
            print

            mode = None
            while mode not in self.modes:
                try:
                    mode = raw_input("> ")[0].lower()
                except IndexError:
                    mode = None
            return mode


    def instructions(self):
        self.__clear()

        print "Mastermind : Instructions"
        print "-" * self.WIDTH
        print "Mastermind is played by two players: the codemaker and the codebreaker."
        print "It is played in a pre-agreed number of games consisting of 12 turns each."
        print
        print "The codemaker forms a secret pattern which the codebreaker must deduce within a game."
        print "The secret pattern consists of 4 codes, allowing duplicates, each of which can be of 6 colours."
        print "The available colours are: red, green, blue, cyan, magenta and yellow."
        print
        print "The codemaker provides feedback on the codebreaker's guesses by:"
        print "    - placing a black key code for each code which has the correct colour and position"
        print "    - placing a white key code for each code which has the correct colour but wrong position"
        print
        print "The codemaker gains a point for each guess made by the codebreaker."
        print "The codemaker gains an extra point if the codebreaker fails to solve the pattern."
        print "The players then take turns playing as the codemaker and codebreaker."
        print
        print "The player with the most points wins."
        print
        print "Colours can be specified by entering the first character of each colour."
        print "    Example > Guess: rgby"
        print
        print "If more than 4 colours is entered, only the first 4 are taken as input."
        print "-" * self.WIDTH
        print

        sys.stdout.flush()
        os.system('read -rs -n 1')


    def options(self):
        while True:
            self.__clear()

            print "Mastermind : Options"
            print "-" * self.WIDTH
            print "[G] Number of games   (must be even, default=2) : %d" % self.games
            print "[P] Number of pegs    (3-8, default=4)          : %d" % self.pegs
            print "[C] Number of colours (3-8, default=6)          : %d" % self.colours
            print "[B] Back"
            print "-" * self.WIDTH
            print

            setting = None
            settings = self.settings.keys()

            while setting not in settings:
                try:
                    setting = raw_input("> ")[0].lower()
                except IndexError:
                    setting = None

            if setting == 'b':
               break

            while True:
                try:
                    value = int(raw_input(">> Enter a new value for %s: " % setting.upper()))
                    if setting == 'g' and is_odd(value):
                        raise 'ParityError'
                    elif (setting == 'p' or setting == 'c') and (value < self.MIN or value > self.MAX):
                        raise 'RangeError'
                except (ValueError, 'ParityError', 'RangeError'):
                    pass
                else:
                    break

            setattr(self, self.settings[setting], value)

    
    def quit(self):
        self.__clear()
        print "Thank you for playing!"
        sys.exit()


    def save_game(self, codemaker, codebreaker, games, turns, length, colours):
        while True:
            try:
                confirm = raw_input("\n\nWould you like to save your game (Y/n)? ")[0].lower()
            except IndexError:
                pass
            else:
                if confirm == 'y':
                    break
                else:
                    return

        saved_games = os.listdir(self.SAVE_DIR)
        if saved_games:
            saved_names = list(saved_games)
            for i, saved_name in enumerate(saved_names):
                saved_names[i] = saved_name.rstrip('.sav')
            print "Saved games found:  %s" % '  '.join(saved_names)

        save_name = raw_input("Enter a name for your save: ").lower()
        
        if save_name in saved_names:
            while True:
                try:
                    confirm = raw_input("%s already exists. Would you like to overwrite (y/N)? " % save_name)[0].lower()
                except IndexError:
                    pass
                else:
                    if confirm == 'y':
                        break
                    else:
                        return

        save_name = os.path.join(self.SAVE_DIR, save_name + '.sav')

        if not os.path.isdir(self.SAVE_DIR):
            os.mkdir(self.SAVE_DIR)

        self.save(save_name, codemaker, codebreaker, games, turns, length, colours)


    def save(self, save_name, codemaker, codebreaker, games, turns, length, colours):
        try:
            save_file = open(save_name, 'w')
        except IOError:
            print "Game cannot be saved. Aborting...\n"
            return

        try:
            pickle.dump(self.games, save_file)
            pickle.dump(self.pegs, save_file)
            pickle.dump(self.colours, save_file)
            pickle.dump(self.turns, save_file)

            pickle.dump(self.guesses, save_file)
            pickle.dump(self.feedback, save_file)
            pickle.dump(self.board, save_file)

            pickle.dump(codemaker, save_file)
            pickle.dump(codebreaker, save_file)

            pickle.dump(games, save_file)
            pickle.dump(turns, save_file)
            pickle.dump(length, save_file)
            pickle.dump(colours, save_file)

        except pickle.PicklingError:
            print "Game cannot be saved. Aborting...\n"
            # delete save file if failed?

        else:
            print "Game saved successfully.\n"

        save_file.close()


    def load_game(self):
        self.__clear()

        print "Mastermind"
        print "-" * self.WIDTH
        print "Searching saved games directory...\n"

        saved_games = os.listdir(self.SAVE_DIR)
        if not saved_games:
            print "No saved games found. Aborting..."
            self.__pause(self.PAUSE)
            return

        saved_names = list(saved_games)
        for i, saved_name in enumerate(saved_names):
            saved_names[i] = saved_name.rstrip('.sav')
        print "Saved games found:  %s\n" % '  '.join(saved_names)

        while True:
            load_name = raw_input("Enter the name of the save you want to load: ").lower() + '.sav'
            if load_name not in saved_games:
                print "Name not found."
            else:
                break

        load_name = os.path.join(self.SAVE_DIR, load_name)
        load_values = self.load(load_name)

        self.play(None, None, True, *load_values)

    
    def load(self, load_name):
        try:
            load_file = open(load_name, 'r')
        except IOError:
            print "Game cannot be loaded. Aborting..."
            self.__pause(self.PAUSE)
            return

        try:
            self.games = pickle.load(load_file)
            self.pegs = pickle.load(load_file)
            self.colours = pickle.load(load_file)
            self.turns = pickle.load(load_file)
            
            self.guesses = pickle.load(load_file)
            self.feedback = pickle.load(load_file)
            self.board = pickle.load(load_file)

            codemaker = pickle.load(load_file)
            codebreaker = pickle.load(load_file)

            games = pickle.load(load_file)
            turns = pickle.load(load_file)
            length = pickle.load(load_file)
            colours = pickle.load(load_file)

        except pickle.UnpicklingError:
            print "Game cannot be loaded. Aborting..."
            self.__pause(self.PAUSE)
            # delete load file if failed?
            load_file.close()

        else:
            load_file.close()
            return (codemaker, codebreaker, games, turns, length, colours)


    def display_game_header(self, codemaker, codebreaker, game, length, colours):
        print "Mastermind : Play : Game (%d/%d)" % (game, self.games)
        print "-" * self.WIDTH
        print "%s will be playing as the codemaker" % codemaker.name
        print "%s will be playing as the codebreaker" % codebreaker.name
        print
        print "Using %d pegs" % length
        print "Using %d colours:" % len(colours),
        for colour in colours:
            print self.colour_names[colour],
        print
        print "-" * self.WIDTH
        print


    def display_turn_header(self, codemaker, codebreaker, game, length, colours, turn=0, last_turn=False):
        if last_turn:
            print "Mastermind : Play : Game (%d/%d)" % (game, self.games)
        else:
            print "Mastermind : Play : Game (%d/%d) : Turn (%d/%d)" % (game, self.games, turn, self.turns)
        print "-" * self.WIDTH
        print "(Codemaker) %-15s : %-7d" % (codemaker.name, codemaker.score),
        print "(Codebreaker) %-15s : %-7d" % (codebreaker.name, codebreaker.score)
        print "Pegs : %-30d" % length,
        print "Colours: %-30s" % ''.join(colours)
        print
        print "Press Ctrl-C to quit and Ctrl-D to save."
        print "-" * self.WIDTH
        print 


    def name_players(self, player1, player2):
        print "Mastermind : Play : Enter your names"
        print "-" * self.WIDTH

        player1.ask_for_name("Hi Player 1! What is your name? ")
        player2.ask_for_name("Hi Player 2! What is your name? ")


    def decide_roles(self, player1, player2):
        players = [player1, player2]
        random.shuffle(players)

        codemaker = players.pop()
        codebreaker = players.pop()

        return codemaker, codebreaker


    def allocate_colours(self):
        return self.colour_codes[:self.colours]

    
    def setup_board(self):
        self.board = []

        board_end = (" " * (self.WIDTH / 4)) + "+" + ("-" * (self.pegs * 3 + 2)) + "+" + ("-" * (self.pegs * 2 + 1)) + "+"
        board_row = (" " * (self.WIDTH / 4)) + "|" + (" " * (self.pegs * 3 + 2)) + "|" + (" " * (self.pegs * 2 + 1)) + "|"

        self.board.append(board_end)
        for row in range(self.turns * 2 + 1):
            self.board.append(board_row)
        self.board.append(board_end)


    def display_board(self):
        print '\n'.join(self.board) + '\n'


    def update_board(self, game):
        guess = list(self.guesses[game]).pop()
        feedback = list(self.feedback[game]).pop()

        board_row = (" " * (self.WIDTH / 4)) + "|  "

        for colour in guess:
            board_row += colour + "  "

        board_row += "| "

        for key in feedback:
            board_row += key + " "

        for empty_key in range(self.pegs - len(feedback)):
            board_row += "  "

        board_row += "|"

        self.board[len(self.guesses[game]) * 2] = board_row

    
    def record_turn(self, game, guess, feedback):
        self.guesses[game].append(guess)
        self.feedback[game].append(feedback)


    def give_game_feedback(self, codemaker, codebreaker):
        if codemaker.is_correct(codebreaker.guess):
            print "Correct, %s!\n" % codebreaker.name
        else:
            print "Fail, %s. Fail.i\n" % codebreaker.name


    def declare_winner(self, player1, player2):
        if player1.score > player2.score:
            winner = player1
        elif player2.score > player1.score:
            winner = player2
        else:
            winner = None

        if winner:
            print "%s wins! Good job!" % winner.name
        else:
            print "It's a tie! Good job!"

    
    def is_last_turn(self, turn):
        return turn == self.turns - 1


    def is_last_game(self, game):
        return game == self.games - 1

    
    def play(self, player1, player2, load_game=False, codemaker=None, codebreaker=None, games=0, turns=0, length=0, colours=[]):
        if not load_game:
            length = self.pegs
            colours = self.allocate_colours()

            self.__clear()

            self.name_players(player1, player2)
            codemaker, codebreaker = self.decide_roles(player1, player2)

        for game in range(games, self.games):
            if not load_game:
                self.guesses[str(game)] = []
                self.feedback[str(game)] = []

                self.setup_board()

                codemaker.reset()
                codebreaker.reset()

                self.__clear()

                self.display_game_header(codemaker, codebreaker, game + 1, length, colours)

                print "%s, DON'T LOOK!" % codebreaker.name.upper()
                codemaker.choose_secret_pattern(length, colours, "%s, choose a secret pattern: " % codemaker.name)

            for turn in range(turns, self.turns):
                if load_game:
                    load_game = False

                self.__clear()

                self.display_turn_header(codemaker, codebreaker, game + 1, length, colours, turn + 1)
                self.display_board()

                while True:
                    try:
                        codebreaker.make_guess(length, colours, "%s, make a guess: " % codebreaker.name)
                    except KeyboardInterrupt:
                        self.save_game(codemaker, codebreaker, game, turn, length, colours)
                        sys.exit()
                    except EOFError:
                        self.save_game(codemaker, codebreaker, game, turn, length, colours)
                    else:
                        break

                if codemaker.is_correct(codebreaker.guess):
                    codemaker.feedback = [' ', ' ', ' ', ' ']

                    self.record_turn(str(game), codebreaker.guess, codemaker.feedback)
                    self.update_board(str(game))

                    break
                else:
                    codemaker.prepare_feedback(codebreaker.guess, self.feedback_keys)

                    print "%s's feedback is" % codemaker.name,
                    codemaker.show_feedback(self.feedback_names)

                    codebreaker.analyse_feedback(codemaker.feedback, length)

                    codemaker.gain_point()
                    if self.is_last_turn(turn):
                        codemaker.gain_point()

                    self.record_turn(str(game), codebreaker.guess, codemaker.feedback)
                    self.update_board(str(game))

                    self.__pause(self.PAUSE)

            self.__clear()

            self.display_turn_header(codemaker, codebreaker, game + 1, length, colours, last_turn=True)
            self.display_board()

            print "%s's secret pattern is" % codemaker.name,
            codemaker.show_secret_pattern(self.colour_names)
            self.__pause(self.PAUSE * 1.5)

            self.give_game_feedback(codemaker, codebreaker)
            self.__pause(self.PAUSE)

            if self.is_last_game(game):
                self.declare_winner(codemaker, codebreaker)
                self.__pause(self.PAUSE)
            else:
                codemaker, codebreaker = codebreaker, codemaker
