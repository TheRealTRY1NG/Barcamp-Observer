from abc import ABC, abstractmethod
from products import Product

# /-------------------------------------------

class CustomerInterface(ABC):

    # TO-DO
    @abstractmethod
    def update(self):
        pass
    
class Customer:

    def __init__(self, p_name: str):
        self._name = p_name

    # TO-DO
    def update(self, p_objectOfInterest: Product):
        print(f"{self._name} now knows that the product '{p_objectOfInterest.name}' is available!")