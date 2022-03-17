from json import dumps, load
from utils.player import Player # the Player class
from utils.shop import Item, Shop # the shop class and items
from os import listdir # for making db.json if non-existent

items_dict = load(open('./db.json'))['shop']
items = {
    key: Item(key, value['price'], value['reward']) for key, value in items_dict.items()
}

def init_db():
    """
    This method will run if the there is no db.json in the directory. This will make sure for no errors
    """
    name = input("Enter you name: ")
    with open('db.json', 'w') as f:
        db = {
                "profile": { "name": name, "bal": 0, "inventory": [] },
                "shop": { "item": { "price": 0, "reward": "" } }
            }
        f.write(dumps(db))
    print("Finished intialising !")

if __name__ == '__main__':
    if 'db.json' not in listdir(): # Checking if db.json exists
        print("\n===Intialising for first time===")
        init_db()
    shop = Shop(items, 'db.json') # Intialising the shop
    player = Player('db.json', shop) # Intialising player object
    while True: # Game loop
        cmd = input("Enter the command: ")
        player.handle(*(cmd.split(" ")))
        print(player.response)
        player.update()