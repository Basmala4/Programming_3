from abc import ABCMeta , abstractmethod

class Iobservable(metaclass=ABCMeta):
    @staticmethod 
    @abstractmethod 
    def Subscribe(observer):
        "the subscribe method"
        
   
    @staticmethod 
    @abstractmethod   
    def Unsubscribe(observer):
        "the unsubscribe method"
        
       
    @staticmethod 
    @abstractmethod 
    def Notify(observer):
        "the notify method"
          

class Subject(Iobservable):
    def __init__(self):
        self._observers = set()
        
    def Subscribe(self,observer):
        self._observers.add(observer)
        
    def Unsubscribe(self, observer):
        self._observers.remove(observer)
        
    def Notify(self , *args):
        for observer in self._observers:
            observer.Notify(*args)
            
class Iobserver(metaclass=ABCMeta):
    @staticmethod 
    @abstractmethod 
    def Notify(subject , *args):
        "receive notification"
      
        
class Observer(Iobserver):
    def __init__(self , subject):
        subject.Subscribe(self)
        
    def Notify(self , *args):
        print(f"observer id : {id(self)} receive {args}")
        
SUBJECT = Subject()
OBSERVER_A = Observer(SUBJECT)
OBSERVER_B = Observer(SUBJECT)

SUBJECT.Notify("first notification" , [1,2,3])
SUBJECT.Unsubscribe(OBSERVER_B)
SUBJECT.Notify("second notification" , {"A" : 1 ,"B" :2 , "C" :3})        
    
        
        
            
          
          
        