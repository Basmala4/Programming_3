from abc import ABCMeta , abstractmethod

class IBuilder(metaclass = ABCMeta) :
    
    @staticmethod
    @abstractmethod   
    def build_part_a():
        "return a"
        
    @staticmethod
    @abstractmethod   
    def build_part_b():
           "return b"
            
    @staticmethod
    @abstractmethod   
    def build_part_c():
        "return c"
        
        
    @staticmethod     
    @abstractmethod 
    def get_result():
        "return all final product"

class Builder(IBuilder):
    def __init__(self):
        self.product = Product()
    
    def build_part_a(self):
        self.product.parts.append("a")
        return self
    
    def build_part_b(self):
        self.product.parts.append("b")
        return self
    
    def build_part_c(self):
        self.product.parts.append("c")
        return self
    
    def get_result(self):
        return self.product

    
class Product():
    def __init__(self):
        self.parts = []
        
        
class Director:
    
    @staticmethod 
    def construct():
        return Builder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()   
                
PRODUCT = Director.construct()
print(PRODUCT.parts)                
        
        
       
    
       
    
    