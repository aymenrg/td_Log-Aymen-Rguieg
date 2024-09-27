import unittest

from exo1 import Item


class TestItem(unittest.TestCase):
    def test_item_initialization(self):
        item = Item(10, 20)
        
        self.assertEqual(item.price, 10)
        self.assertEqual(item.weight, 20)

if __name__ == '__main__':
    unittest.main()
