#Adapter

class ClassA():
    def method_a(self):
        print("method A")
        
        
class ClassB():
    def method_b(self):
        print("method B")
        
        
        
class ClassABadapter():
    def __init__(self):
        self.class_b = ClassB()
    

    def method_a(self):
        self.class_b.method_b()
        
     
        
     
ITEMS = [ClassA(), ClassB()] 
for item in ITEMS :
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()
        
ITEMS = [ClassA() , ClassABadapter()] 
for item in ITEMS:
    item.method_a()
       
        
        
       
        
        
        