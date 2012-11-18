#!/usr/bin/env python

"""The Mastermind project."""

import signal

from mastermind_game import MastermindGame
from signal_handler import quit_game

def main():
    """Main program loop."""
    signal.signal(signal.SIGINT, quit_game)  # Exit gracefully

    mastermind = MastermindGame()
    mastermind.main()


if __name__ == '__main__':
    main()
