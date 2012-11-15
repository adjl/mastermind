import os
import sys

def quit_game(signal, frame):
    os.system('clear')
    print "Thank you for playing!"
    sys.exit()
