from abc import ABC, abstractmethod

class ChildInterface(ABC):

    @abstractmethod
    def update(self, objectOfInterest):
        pass