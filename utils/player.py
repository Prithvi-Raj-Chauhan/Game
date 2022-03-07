from utils.mini_games.RandomNumberGuesser import RandomNumberGuesser


class Player:
    def __init__(self, name: str, bal: int) -> None:
        self.name = name
        self.bal = bal
        self.msg = ""

    def cmd(self, prompt):
        inp = input(prompt)
        self.handle(inp)

    def handle(self, inp: str):
        if inp == 'profile': self.react(profile(self))
        elif inp == 'exit': self.exit()
    
    def react(self, msg: str):
        self.msg = msg

    @property
    def response(self):
        return self.msg

    def addMoney(self, amount: int):
        self.bal += amount
    
    def subMoney(self, amount: int) -> bool:
        if amount<self.bal:
            self.bal -= amount
            return True
        else:
            return False

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

def profile(p: Player):
    profile = p.generateProfile()
    return f"\n\tName: \t{profile['name']}\n\tBalance: \t{profile['bal']}\n"