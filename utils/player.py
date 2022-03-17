from json import load, dump

class Player:
    def __init__(self, path: str, shop) -> None:
        self.path = path
        self.data: dict[str, dict] = load(open(path))
        self.name = self.data['profile']['name']
        self.bal = self.data['profile']['bal']
        self.inv = self.data['profile']['inventory']
        self.msg = ""

        self.shop = shop

    def handle(self, inp: str, param = None):
        if inp == 'profile': self.react(profile(self))
        elif inp == 'exit': self.exit()
        elif inp == 'beg': self.beg()
        elif inp == 'buy': self.buy(param)
        elif inp == 'inv': self.react("\n".join(self.inv))
    
    def react(self, msg: str):
        self.msg = msg

    @property
    def response(self):
        return self.msg

    def addMoney(self, amount: int, msg: str = ""):
        self.bal += amount
        if not msg:
            self.react(f"Added amount {amount}")
        else:
            self.react(msg)
    
    def subMoney(self, amount: int) -> bool:
        if amount<self.bal:
            self.bal -= amount
            return True
        else:
            return False

    def beg(self):
        from random import randint
        chance = randint(1,100)
        if not chance % 5:
            self.addMoney(5000, "You beggar take this money!")
        else: self.react("You jerk get lost!")

    def buy(self, item):
        if item not in self.inv:
            self.inv.append(self.shop.buy(item))
            self.react(f"Successfully bought {item}!")
        else:
            self.react(f"You already have a {item}! Don't be greedy.")

    def generateProfile(self) -> dict:
        return {
            'name': self.name,
            'bal': self.bal
        }

    def exit(self):
        import time
        print("Exiting in 3 seconds...")
        time.sleep(3)
        exit()

    def update(self):
        self.msg = str()
        self.data['profile']['name'] = self.name
        self.data['profile']['bal'] = self.bal
        self.data['profile']['inventory'] = self.inv
        dump(self.data, open(self.path, 'w'))

def profile(p: Player):
    profile = p.generateProfile()
    return f"\n\tName: \t{profile['name']}\n\tBalance: \t{profile['bal']}\n"