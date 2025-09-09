from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def update(self, p_objectOfInterest):
        pass
    
class Mother(Parent):

    # Do something when p_objectOfInterest changes
    def update(self, p_objectOfInterest):
        print(f"New location of my child: {p_objectOfInterest}")
