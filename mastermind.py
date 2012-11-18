#!/usr/bin/env python

"""The Mastermind project."""

import signal

from mastermind_game import MastermindGame
from signal_handler import quit

def main():
    signal.signal(signal.SIGINT, quit)  # Exit gracefully

    mastermind = MastermindGame()
    mastermind.main()


if __name__ == '__main__':
    main()
