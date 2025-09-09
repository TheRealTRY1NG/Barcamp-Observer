from parents import Parent

class Child():

    def __init__(self):

        self.parents: list[Parent] = []
        self.location: str = ""

    # Add subscriber
    def addParent(self, parent):
        self.parents.append(parent)

    # Remove subscriber
    def removeParent(self, parent):
        self.parents.remove(parent)

    # Inform subscribers
    def sendLocationUpdate(self):
        for par in self.parents:
            par.update(self.location)

    def setLocation(self, newLocation):
        self.location = newLocation
        self.sendLocationUpdate()
