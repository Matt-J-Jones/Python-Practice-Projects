from lib.shoppingbasket import ShoppingBasket

def test_createShoppingBasket():
    basket = ShoppingBasket()
    assert basket.items == []
    assert basket.total == 0

def test_additem():
    basket = ShoppingBasket()
    basket.addItem("Chocolate", 1.00)
    assert len(basket.items) == 1
    assert basket.total == 1.00

def test_addTwoItems():
    basket = ShoppingBasket()
    basket.addItem("Chocolate", 1.00)
    basket.addItem("Sherbert", 2.00)
    assert len(basket.items) == 2
    assert basket.total == 3.00

def test_addTwoItemsReturnsTotal():
    basket = ShoppingBasket()
    basket.addItem("Chocolate", 1.00)
    basket.addItem("Sherbert", 2.00)
    assert len(basket.items) == 2
    assert basket.returnTotal() == 3.00

def test_addTwoItemsReturnsList():
    basket = ShoppingBasket()
    basket.addItem("Chocolate", 1.00)
    basket.addItem("Sherbert", 2.00)
    assert len(basket.items) == 2
    assert basket.returnTotal() == 3.00
    assert basket.returnList() == ["Chocolate", "Sherbert"]