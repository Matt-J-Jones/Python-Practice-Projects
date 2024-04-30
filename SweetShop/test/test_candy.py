from lib.candy import Candy

def test_candy():
    candy = Candy("Chocolate", 1.00)
    assert candy.getName() == "Chocolate"
    assert candy.getPrice() == 1.00