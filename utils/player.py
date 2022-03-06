from utils.mini_games.RandomNumberGuesser import RandomNumberGuesser

class Player:
    def __init__(self, name: str, bal: int) -> None:
        self.name = name
        self.bal = bal
        self.msg = ""
    
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