import os
import sys

def quit(signal, frame):
    os.system('clear')
    print "Thank you for playing!"
    sys.exit()
