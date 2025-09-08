from parent import Parent

class Mother(Parent):

    def __init__(self):
        return

    def update(self, objectOfInterest):
        print(f"New location of my child: {objectOfInterest}")
