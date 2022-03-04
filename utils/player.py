class Player:
    def __init__(self, name: str, bal: int) -> None:
        self.name = name
        self.bal = bal
    
    def addMoney(self, amount: int):
        self.bal += amount
    
    def subMoney(self, amount: int) -> bool:
        if amount<self.bal:
            self.bal -= amount
            return True
        else:
            return False