from mother import Mother
from child import Child

if __name__ == "__main__":
    exampleMother = Mother()
    exampleChild = Child()

    exampleChild.addParent(exampleMother)
    print("Update:")
    exampleChild.setLocation("At home")

    exampleChild.removeParent(exampleMother)
    print("Update:")
    exampleChild.setLocation("School")

