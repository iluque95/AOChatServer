from utilities import *

class User:
    
    def __init__(self, s):
        self.socket = s
        #self.queue = []
        self.inputQ = deque()
        self.outputQ = deque()
        self.userIndex = 0
        self.map = 0
        self.area = 0
        
        self.name = ""
        self.position = 0
        self.token = ""
        
        self.hThread = start_new_thread(self.handle_reception, (self.socket,))
     
        
     
    # thread function 
    def handle_reception(self,c): 
        while True: 
  
            # data received from client 
            try:
            
                data = c.recv(1024)
                
                if not data: 
                
                    tsPrint('Bye') 
                    
                    break
                
                self.inputQ.append(data)

                #tsPrint ("Received: " + str(data))
                
                
                # reverse the given string from client 
                #data = data[::-1]
                
                '''
                data = ('HTTP/1.1 200 OK\r\n'
                    'Server: Python Game Chat Backend\r\n'
                    'Accept-Ranges: bytes\r\n'
                    'Content-Length: 12\r\n'
                    'Connection: close\r\n'
                    'Content-Type: text/html\r\n\r\n'
                    'Hello World!\r\n\r\n').encode('ascii')
                '''
                
            except Exception as e:
    
                tsPrint("An exception occurred: " + str(e))
                break
  
        # connection closed 
        c.close() 
        
        tsPrint("Connection closed")

        
        

        
    