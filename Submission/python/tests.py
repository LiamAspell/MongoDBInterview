import unittest                                      
from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing

class ShoppingCartTest(unittest.TestCase):
    #Task 1 
    def test_on_totals_1(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 5)
        sc.add_item("apple", 6)
        sc.add_item("pear", 3)
        sc.add_item("avacado", 4)
        with Capturing() as output:
            sc.print_receipt(2)                                                      
        self.assertEqual("100 - 5 - apple", output[0])                  
        self.assertEqual("100 - 6 - apple", output[1])
        self.assertEqual("0 - 3 - pear", output[2])   
        self.assertEqual("400 - 4 - avacado", output[3])
        self.assertEqual("2700 - Total", output[4])
        
    def test_on_totals_2(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        sc.add_item("apple", 5)
        with Capturing() as output:
            sc.print_receipt(1)                                         
        self.assertEqual("banana - 5 - 200", output[0])                                   
        self.assertEqual("pear - 5 - 0", output[1])                     
        self.assertEqual("apple - 5 - 100", output[2])
        self.assertEqual("Total - 1500", output[3])
        
    def test_on_totals_3(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("banana", 3)
        sc.add_item("avacado", 10)
        with Capturing() as output:
            sc.print_receipt(2)                                         
        self.assertEqual("200 - 3 - banana", output[0])                 
        self.assertEqual("400 - 10 - avacado", output[1])
        self.assertEqual("4600 - Total", output[2])
    
    #Task 2 
    def test_on_each_individual_item_scanned_1(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("pear", 7)
        sc.add_item("apple", 16)
        sc.add_item("avacado", 10)
        with Capturing() as output:
            sc.print_receipt(1)
        self.assertEqual("pear - 7 - 0", output[0])
        self.assertEqual("apple - 16 - 100", output[1])
        self.assertEqual("avacado - 10 - 400", output[2])
        
    def test_on_each_individual_item_scanned_2(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("banana", 3)
        sc.add_item("apple", 2)
        sc.add_item("pear", 5)
        sc.add_item("avacado", 10)
        with Capturing() as output:
            sc.print_receipt(1)
        self.assertEqual("banana - 3 - 200", output[0])
        self.assertEqual("apple - 2 - 100", output[1])
        self.assertEqual("pear - 5 - 0", output[2])
        self.assertEqual("avacado - 10 - 400", output[3])
    
    #Task 3 
    def test_on_regular_format(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("banana", 5)
        sc.add_item("apple", 2)
        sc.add_item("pear", 5)
        sc.add_item("apple", 5)
        sc.add_item("avacado", 10)
        with Capturing() as output:
            sc.print_receipt(1)
        self.assertEqual("banana - 5 - 200", output[0])
        self.assertEqual("apple - 2 - 100", output[1])
        self.assertEqual("pear - 5 - 0", output[2])
        self.assertEqual("apple - 5 - 100", output[3])
        self.assertEqual("avacado - 10 - 400", output[4])
        self.assertEqual("Total - 5700", output[5])
        
    def test_on_alternative_format(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("banana", 3)
        sc.add_item("apple", 2)
        sc.add_item("pear", 5)
        sc.add_item("apple", 3)
        sc.add_item("avacado", 10)
        with Capturing() as output:
            sc.print_receipt(2)                                         
        self.assertEqual("200 - 3 - banana", output[0])                 
        self.assertEqual("100 - 2 - apple", output[1])                  
        self.assertEqual("0 - 5 - pear", output[2])                     
        self.assertEqual("100 - 3 - apple", output[3])
        self.assertEqual("400 - 10 - avacado", output[4])
        self.assertEqual("5100 - Total", output[5])

unittest.main(exit=False)
