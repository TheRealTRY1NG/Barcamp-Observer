from abc import ABC, abstractmethod
from products import Product

# /-------------------------------------------

class CustomerInterface(ABC):

    # To-Do
    ...
    
class Customer:

    def __init__(self, p_name: str):
        self._name = p_name

    # To-Do
    ...