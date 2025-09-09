from parents import Mother
from child import Child

if __name__ == "__main__":

    # Creating a mother and a child
    exampleMother = Mother()
    exampleChild = Child()

    # Binding the mother as a parent to the child ("subscribing")
    exampleChild.addParent(exampleMother)

    # On a change of the subscripted interest subscribers will be notified now!
    exampleChild.setLocation("At home")

