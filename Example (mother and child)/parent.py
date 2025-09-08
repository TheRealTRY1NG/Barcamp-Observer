from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def update(self, objectOfInterest):
        pass