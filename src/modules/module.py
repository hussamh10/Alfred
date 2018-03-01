from abs import ABC, absctractmethod

class Module(ABC):

    def __init__(self, name):
        self.name = name

    @absctractmethod
    def getAnswer(self, query, alfred):
        pass