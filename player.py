from functions import remove_empty_elements

class Player(object):
    def __init__(self):
        self.name = ''
        self.score = 0


    def __validate_input(self, message):
        pattern = raw_input(message)[:self.pattern_length].lower()

        if len(pattern) < self.pattern_length:
            return

        for colour in pattern:
            if colour not in self.pattern_colours:
                return

        return list(pattern)


    def remember_rules(self, pattern_length, pattern_colours):
        self.pattern_length = pattern_length
        self.pattern_colours = pattern_colours


    def ask_for_name(self, message=''):
        self.name = None
        while not self.name:
            self.name = raw_input(message).lower().capitalize()


    def choose_secret_pattern(self, message=''):
        self.secret_pattern = None
        while not self.secret_pattern:
            self.secret_pattern = self.__validate_input(message)


    def make_guess(self, message=''):
        self.guess = None
        while not self.guess:
            self.guess = self.__validate_input(message)


    def is_correct(self, guess):
        return guess == self.secret_pattern


    def prepare_feedback(self, guess, feedback_keys):
        self.feedback = []

        guess = list(guess)
        secret_pattern = list(self.secret_pattern)

        for i, colour in enumerate(guess):
            if colour == secret_pattern[i]:
                self.feedback.append(feedback_keys['correct'])
                guess[i] = secret_pattern[i] = None

        remove_empty_elements(guess)
        remove_empty_elements(secret_pattern)

        for i, colour in enumerate(guess):
            if colour in secret_pattern:
                self.feedback.append(feedback_keys['partially_correct'])
                secret_pattern[secret_pattern.index(colour)] = None


    def show_feedback(self, feedback_names):
        if self.feedback:
            feedback = []
            for key in self.feedback:
                feedback.append(feedback_names[key])
            print ' '.join(feedback)
        else:
            print 'none'


    def analyse_feedback(self, feedback):
        pass


    def show_secret_pattern(self, colour_names):
        secret_pattern = []
        for colour in self.secret_pattern:
            secret_pattern.append(colour_names[colour])
        print ' '.join(secret_pattern)


    def gain_point(self):
        self.score += 1
