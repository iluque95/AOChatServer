
# import socket programming library 

from user import *

global htConnection
isRunning = True

users = list()


def handle_connections(s):

    # a forever loop until client wants to exit 
    while isRunning: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        tsPrint('Connected to :' + addr[0] + ':' + str(addr[1])) 
        
        newUser = User(c)
        
        now = datetime.datetime.now()
                
        data = "Hello I am the server. Time: " + now.strftime("%H:%M:%S %d/%m/%Y")

        newUser.outputQ.append(data)
        
        users.append(newUser)
        # Send Welcome message to client
        #msg = "Welcome "
        #c.send(bytes(msg+'\0','ascii'))
        
        

 
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening")

    # Start a new thread to handle new connections
    htConnection = start_new_thread(handle_connections, (s,))

    while True:
        
        for i in users:

            # Check if users has pending data to process

            # Send updates
            while i.outputQ:
                msg = i.outputQ.popleft()
                i.socket.send(bytes(msg+'\0','ascii'))
                tsPrint("Data sent:" + str(msg))
                
                
        time.sleep(0.5)
    
    isRunning = False 
    s.close() 
  
if __name__ == '__main__': 
    Main() 
