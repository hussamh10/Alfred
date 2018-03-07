from controller import parse

class Alfred():

    def __init__(self):
        self.busy = False
        self.setupNotifiers()
        pass

    def isBusy(self):
        return self.busy

    def askQuestion(self, query):
        module, query = parse(query)
        return module.getAnswer(query, self)

    def askUser(self, query):
        return input()

    def setupNotifiers(self):
        '''
        for setting up modules like timer and alarm
        '''
        pass

    def tick(self):
        '''
        to be called in a for loop by the gui
        '''
        pass

a = Alfred()
print(a.askQuestion('toss'))
