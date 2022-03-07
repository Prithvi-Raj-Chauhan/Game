import random
from utils.player import Player

if __name__ == '__main__':
    player = Player('Prithvi Raj Chauhan', 5000) 
    while True:
        player.cmd("Enter the command: ")
        print(player.response)
        player.update()