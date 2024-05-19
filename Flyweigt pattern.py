class ComplexCars(object):
    def __init__(self):
        pass
    
    def cars(self, car_name):
        return("complex pattern[%s]"%(car_name))
    
class CarFamilies(object):
    
    car_family= {}
    
    def __new__(cls , name , car_family_id):
        
        try:
            obj = cls.car_family[car_family_id]
       
        except KeyError:
            obj = object.__new__(cls)
            obj = cls.car_family[car_family_id]
            
        return obj     
    
    def set_car_info(self, car_info):
        cg = ComplexCars()
        self.car_info = cg.cars(car_info)
        
    def get_car_info(self):
       return(self.car_info)
   
    
if __name__ == "__main__" :
    car_data =(('a',1,'audio') , ('a',2,'ferrari' , ('b',1,'audio')))
    car_family_objects = []
    
for i in car_data :
    obj = CarFamilies(i[0] , i[1])
    obj.set_car_info(i[2])
    car_family_objects.append(obj)
    
for i in car_family_objects:
    print("id = "+ str(id(i)))
    print(i.get_car_info())
    
    
    
     
     
          
    

