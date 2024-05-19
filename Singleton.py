import copy

class singleton():
    value = []
    
    def __new__(cls):
        return cls
    
    @staticmethod 
    def static_method():
        
     @classmethod 
     def class_method(cls):
        print(cls.value)
    
print(f"id(singleton)\t={id(singleton)}")


obj1 = singleton()
print(f"id(obj1)\t={id(obj1)}")

obj2 = copy.deepcopy(obj1)
print(f"id(obj2)\t={id(obj2)}")

obj3 = singleton()
print(f"id(obj3)\t={id(obj3)}")