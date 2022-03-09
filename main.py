from json import dumps
from utils.player import Player # the Player class
from os import listdir # for making db.json if non-existent

def init_db():
    name = input("Enter you name: ")
    with open('db.json', 'w') as f:
        db = {
"profile": { "name": name, "bal": 0, "inventory": [] },
"shop": { "item": { "price": 0, "type": "" } }
}
        f.write(dumps(db))
    print("Finished intialising !")

if __name__ == '__main__':
    if 'db.json' not in listdir():
        print("\n===Intialising for first time===")
        init_db()
    player = Player('db.json') 
    while True:
        player.cmd("Enter the command: ")
        print(player.response)
        player.update()