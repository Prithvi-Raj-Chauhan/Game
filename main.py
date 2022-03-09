from utils.player import Player

if __name__ == '__main__':
    player = Player('db.json') 
    while True:
        player.cmd("Enter the command: ")
        print(player.response)
        player.update()