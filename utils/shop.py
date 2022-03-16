class Item:
    def __init__(self, name: str, price: int, reward: int) -> None:
        self.name = name
        self.price = price
        self.reward = reward

    def __repr__(self) -> str:
        return f"Item: {self.name}; Price: {self.price}"

    def use(self) -> int:
        return self.reward

    def sell(self) -> int:
        return self.price*.01*self.reward
    
    def representAsDict(self) -> dict:
        return {"price": self.price, "reward": self.reward}

class Shop:
    def __init__(self, items: list[Item] | dict[str, Item], path) -> None:
        from json import load
        self.data:dict = load(open(path))
        if type(items) == list:
            self.items = items
        elif type(items) == dict:
            self.items = [item for item in items.values()]
        else:
            raise TypeError("Error! Expected items to be a list or a dict.")
        self.shop = self.data['shop']
        for item in self.items:
            self.shop[item] = item.representAsDict()
        self.data['shop'] = self.shop

    def buy(self, item:Item):
        return item if (item in [item.name for item in self.items]) else False

    def commit(self):
        from json import dump
        dump(self.data, open(self.path, 'w'))

SHOVEL = Item("shovel", 50000, 5000)

ITEMS = {
    'shovel': SHOVEL
}

if __name__ == '__main__':
    print(SHOVEL.representAsDict())