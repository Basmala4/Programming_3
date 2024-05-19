class Memento:
    def __init__(self,file,content):
        self.file = file
        self.content = content
        
class X:
    def __init__(self , file_path):
        self.file = file_path
        self.content = ""
        
    def Write(self , string):
       self.content += string
       
    def Save(self):
        return Memento(self.file,self.content)
    
    def Undo(self, memento):
        self.file = memento.file
        self.content = memento.content
        
class Y  :
    def Save(self , x):
        self.mem = x.Save()
        
    def Undo(self , x):
        x.Undo(self.mem)
        
if __name__=="__main__":
    y= Y()
    x= X("GFG.txt")
    
    x.Write("first vision of data\n")
    print(x.content + "\n\n")
    
    y.Save(x)
    
    x.Write("Second vision of data\n")
    print(x.content + "\n\n")
    
    y.Undo(x)
    print(x.content + "\n\n")
    
    

        
      
       
        