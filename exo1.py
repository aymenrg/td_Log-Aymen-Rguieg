"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""
class Item:
    def __init__(self,price,weight):
        self.price=price
        self.weight=weight
Item1 = Item(10,20)
print(Item1.price)
print(Item1.weight)