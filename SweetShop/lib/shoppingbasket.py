from . import candy

class ShoppingBasket:
    def __init__(self):
        self.items = []
        self.total = 0

    def addItem(self, item, price):
        self.items.append(candy.Candy(item, price))
        self.total += price

    def returnTotal(self):
        return self.total

    def returnList(self):
        shoppingList = []
        for item in self.items:
            shoppingList.append(item.getName())
        return shoppingList
