from module import Module
from subprocess import check_output

#BIGTODO make cross platform
#BIGTODO remove gcal dependency or integrate fully

class Calendar(Module):
    def __init__(self):
        super(Calendar, self).__init__("Calendar")

    def getAnswer(self, query, alfred):
        query = query.lower().split()

        if 'week' in query:
            return self.weekAgenda()

        if 'next' in query:
            return self.nextEvent()

        if 'agenda' in query:
            return self.todayAgenda()
    

    def nextEvent(self):
        #TODO
        pass

    def weekAgenda(self):
        #TODO
        pass

    def todayAgenda(self):
        output = check_output(['gcalcli', 'agenda'])
        return output

