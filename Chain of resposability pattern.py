class Request:
    def __init__(self, data):
        self.data = data
        self.valid = True
        
class RequestHandler:
    def __init__(self , successor = None):
        self.successor = successor
        
    def handle_request(self , request):
        if self.successor:
            self.successor.handle_request(request)
            
class AuthenticationHandler(RequestHandler) :
    def handle_request(self, request):
        if "token" not in request.data:
            request.valid = False
            print("AuthenticationHandler is failed")
        print("AuthenticationHandler Done..")
        super().handle_request(request)
            
        
class DataValidationHandler(RequestHandler):
    def handle_request(self, request):
        if not request.valid:
            return
        if "data" not in request.data:
            request.valid = False
            print("DataValidationHandler is failed")
        print("DataValidationHandler Done..")
        super().handle_request(request)
            
       
class LogginHandler(RequestHandler):
    def handle_request(self, request):
        if not request.data:
            return
        print("Loggin request")
        super().handle_request(request)
        
        
if __name__ == "__main__" :
    request = Request({"token":"abc123" , "data":"some_data"})

Authentication = AuthenticationHandler()
Validation = DataValidationHandler(Authentication)
Loggin = LogginHandler(Validation)
Loggin.handle_request(request)

if request.valid:
    print("Request proccessing successfuly")
else:
    print("Request proccessing failed")
    
       
        
       
        
        
            
        
           
        