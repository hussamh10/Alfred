from abc import ABC, abstractmethod

class Module(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def getAnswer(self, query, alfred):
        pass