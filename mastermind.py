#!/usr/bin/env python

from player import Player
from computer_player import ComputerPlayer
from game import Game

def main():
    game = Game()
    while True:
        mode = game.menu()
        if mode == 's':
            game.play(player1=Player(), player2=ComputerPlayer())
        elif mode == 'm':
            game.play(player1=Player(), player2=Player())
        elif mode == 'd':
            game.play(player1=ComputerPlayer(), player2=ComputerPlayer())
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
