#!/usr/bin/env python

from player import Player
from computer_player import ComputerPlayer
from game import Game

def main():
    game = Game()
    while True:
        mode = game.menu()
        if mode == 's':
            game.play(Player(), ComputerPlayer())
        elif mode == 'm':
            game.play(Player(), Player())
        elif mode == 'd':
            game.play(ComputerPlayer(), ComputerPlayer())
        elif mode == 'c':
            game.load_game()
        elif mode == 'i':
            game.instructions()
        elif mode == 'o':
            game.options()
        elif mode == 'q':
            game.quit()


if __name__ == '__main__':
    main()
