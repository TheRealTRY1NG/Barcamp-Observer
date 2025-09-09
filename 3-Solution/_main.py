from webshop import Webshop
from products import *
from customer import Customer

# /-------------------------------------------

if __name__ == "__main__":

    # Creating the webshop
    coolShop = Webshop()

    # Adding some customers
    randomCustomer1 = Customer("Tyler")
    randomCustomer2 = Customer("Maria")

    # TO-DO: Task 1
    coolShop.addSubEvery(randomCustomer1)
    coolShop.addSubEvery(randomCustomer2)
    
    # Adding some products
    niceShoes = Shoes("Soccer shoes", "Nike", "White", 44, "Spikes", True)
    evenNicerShoes = Shoes("Tennis shoes", "Asics", "Green", 46, "Flat")
    niceTrousers = Trouser("Jeans", "Levi Strauss", "Blue", 32, 34)
    niceJacket = Jacket("Hoody", "Adidas", "Black", 60, True)
    coolShop.addProducts([niceShoes, evenNicerShoes, niceTrousers, niceJacket])


    # TASK 1:
    # Both customers want to know when any kind of available product is added to the shop.
    # Build in the observer pattern to automatically inform them about it. 

    # TASK 2:
    # randomCustomer1 wants to know when some of those evenNicerShoes are available again.
    # Build in the observer pattern to automatically inform them when their availability changes. 

    # TASK 3:
    # randomCustomer2 wants to know when any kind of shoes with flat soles are available again.
    # Build in the observer pattern to automatically inform them when their availability changes. 
    

    