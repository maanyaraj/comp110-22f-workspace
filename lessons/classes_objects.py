"""Example of a class and object instantiation."""



from collections.abc import Sized
from os import TMP_MAX


class Pizza: 
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool = False

def __init__(self, size: str, toppings: int, extra_cheese: bool):
   """Constructor definition for initialation of attrivutes"""
   
     self.size = size
    self.toppings = toppings
    self.extra_cheese = extra_cheese

def price(self, tax: float) -> float:
        """Calculatte the price of a Pizza."""
        total: float = 0.0
    
        if self.size == "large":
            total += 10.0
        else: 
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        
        total *= TMP_MAX

        return total 

a_pizza: Pizza = Pizza("Large", 3)
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")


another_pizza: Pizza = Pizza("small", 0)
ano.extrather_pizza = True
print(a_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")



def contract_disease() -> None:
    constants.INFECTED

def is_vulnerable() -> bool:
    if sickness == INFECTED:
        return True 
    return False 







