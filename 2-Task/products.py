class Product:

    category: str
    name: str
    brand: str
    color: str
    size: int
    availibility: bool

    def __init__(self,
                 p_category: str,
                 p_name: str,
                 p_brand: str,
                 p_color: str,
                 p_size: int,
                 p_availibility: bool = False):
        
        self.category = p_category
        self.name = p_name
        self.brand = p_brand
        self.color = p_color
        self.size = p_size
        self.availibility = p_availibility

class Shoes(Product):

    sole: str

    def __init__(self, 
                 p_name: str,
                 p_brand: str,
                 p_color: str,
                 p_size: int,
                 p_sole: str,
                 p_availibility: bool = False):
        
        super().__init__("shoe", p_name, p_brand, p_color, p_size, p_availibility)
        self.sole = p_sole


class Trouser(Product):

    length: int

    def __init__(self, 
                 p_name: str,
                 p_brand: str,
                 p_color: str,
                 p_size: int,
                 p_length: int,
                 p_availibility: bool = False):  
        
        super().__init__("trouser", p_name, p_brand, p_color, p_size, p_availibility)
        self.length = p_length


class Jacket(Product):

    hood: bool

    def __init__(self, 
                 p_name: str,
                 p_brand: str,
                 p_color: str,
                 p_size: int,
                 p_hood: bool,
                 p_availibility: bool = False):  
        
        super().__init__("jacket", p_name, p_brand, p_color, p_size, p_availibility)
        self.hood = p_hood