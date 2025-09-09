from products import *
from customer import Customer

# /-------------------------------------------

class Webshop:

    # All product sorted by category
    products: dict[str, list[Product]] = {}

    # TO-DOs

#    ________________________________________________________________
#   /
#  /    BUSINESS-LOGIC
# /

    def _exists(self, p_product: Product) -> bool:
        if p_product in self.products[p_product.category]:
            return True

    def addProduct(self, new_product: Product):
        # Create new list for that category
        if new_product.category not in self.products.keys():
            self.products[new_product.category] = []

        # Add new product if possible
        if not self._exists(new_product):
            self.products[new_product.category].append(new_product)

    def addProducts(self, new_products: list[Product]):
        if new_products:
            for p in new_products:
                self.addProduct(p)

    def changeAvailibility(self, p_product: Product, new_availibility: bool):  
        # Change availibility if possible
        if self._exists(p_product):
            self.products[p_product.category][self.products[p_product.category].index(p_product)].availibility = new_availibility


    def removeProduct(self, p_product: Product):
        # Remove product if possible
        if self._exists(p_product):
            self.products[p_product.category].remove(p_product)
