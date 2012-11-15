#!/usr/bin/env python

import signal

from mastermind_game import MastermindGame
from signal_handler import quit_game

def main():
    signal.signal(signal.SIGINT, quit_game)

    mastermind = MastermindGame()
    mastermind.main()


if __name__ == '__main__':
    main()
