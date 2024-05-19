#Factory


class ConcreteProductA():
    def __init__(self):
        self.name = "concreteproductA"
        
class ConcreteProductB():
    def __init__(self):
        self.name ="concreteproductB"
        
class ConcreteProductC():
    def __init__(self):
        self.name = "concreteproductC"
        
        
class Creator:
    
    @staticmethod
     
    def create_opject(some_property):
        if some_property == "a":
          return ConcreteProductA()
        if some_property == "b" :
            return ConcreteProductB()
        if some_property == "c" :
            return ConcreteProductC()
   
        return None 

#CLIENT
PRODUCT = Creator.create_opject("b")
print(PRODUCT.name)    
          
        
        
        
        