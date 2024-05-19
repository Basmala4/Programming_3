class Washing:
    def wash(self):
        print("washing..")
        
class Rinsing:
    def rinse(self):
        print("rinsing..")
        
class Spinning:
    def spine(self):
        print("spinning..")
        
        
class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spnning = Spinning()
        
        
    def StartWashing(self):
       self.washing.wash()
       self.rinsing.rinse()
       self.spnning.spine()
       
       
#main method

if __name__ == "__main__" :
    washingMachine = WashingMachine()
    washingMachine.StartWashing()
       
        
        
        

