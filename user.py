from utilities import *
from channel import *
from channels import *
from observer import *

class User(Observer):
    
    def __init__(self, s, c):
        self.socket = s
        #self.queue = []
        self.inputQ = deque()
        self.outputQ = deque()
        self.userIndex = 0
        self.map = 0
        self.area = 0
        self.channels = list()
        self.name = ""
        self.position = 0
        self.token = ""
        
        self.hThread = start_new_thread(self.handle_reception, (self.socket,))

        self.disconnectionCallback = c

    def __del___(self):

        tsPrint("Destroying client...")
     
    # thread function 
    def handle_reception(self, c): 
        while True: 
  
            # data received from client 
            try:
            
                data = c.recv(1024)
                
                if not data:
                    break
                
                self.channels[0].addPacket(data)
                #self.inputQ.append(data)

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

        tsPrint("[" + c.getpeername()[0] + ":" + str(c.getpeername()[1]) + "] connection closed.")
        
        # connection closed 
        c.close()

        # Unsubscribe
        for i in self.channels:
           i.detach(self)

        self.disconnectionCallback(self)

    def update(self, channelId, msg) -> None:

        self.socket.send(msg)