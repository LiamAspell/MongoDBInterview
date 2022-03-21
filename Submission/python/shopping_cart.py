from abc import ABC, abstractmethod
from ast import And
from re import X
from typing import Dict, Mapping

from shopping_cart_interface import IShoppingCart
from pricer import Pricer


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer):
        self.pricer = pricer
        self._contents: Dict[str,int] = {}
        self._keys=self._contents.keys() 
        self._format=1
        self._list=[]

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        if item_type not in self._contents:
            self._contents[item_type] = number
            self._list.append(item_type)
            self._list.append(number)
            return self._list
        else:
            self._contents[item_type] = self._contents[item_type] + number
            self._list.append(item_type)
            self._list.append(number)
            return self._list
                       
    def print_receipt(self, format):
        
        
        
        total = 0
        i = 0
        while i < len(self._list):
            x = self._list[i]
            y = self._list[i+1]
            z = self.pricer.get_price(x)
            if format == 1:
                print(f'{x} - {y} - {z}')
            elif format == 2:
                print(f'{z} - {y} - {x}')
            i = i +2
        
        for key, value in self._contents.items():
             price = self.pricer.get_price(key)
             total += (value * price)
    
        if format == 1:
            print(f'Total - {total}')
        elif format == 2: 
            print(f'{total} - Total')            
     
                    
class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method()

class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """
    def factory_method(self) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer())
