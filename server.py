
# import socket programming library 
import socket 
import datetime
  
# import thread module 
from _thread import *
import threading 
  
print_lock = threading.Lock()

# CRAW; 09/02/2021 --> ThreadSafe
def tsPrint(msg):
    # lock acquired by client 
    print_lock.acquire()
    print(msg)
    # lock released on exit 
    print_lock.release() 
  
# thread function 
def threaded(c): 
    while True: 
  
        # data received from client 
        try:
            
            data = c.recv(1024)
            
            if not data: 
                
                tsPrint('Bye') 
                
                break
                
            tsPrint ("Received: " + str(data))
            
            
            # reverse the given string from client 
            #data = data[::-1]
            
            """
            data = ('HTTP/1.1 200 OK\r\n'
                'Server: Python Game Chat Backend\r\n'
                'Accept-Ranges: bytes\r\n'
                'Content-Length: 12\r\n'
                'Connection: close\r\n'
                'Content-Type: text/html\r\n\r\n'
                'Hello World!\r\n\r\n').encode('ascii')
            """
            
            now = datetime.datetime.now()
            
            data = ("Hello I am the server. Time: " + now.strftime("%H:%M:%S %d/%m/%Y")).encode('ascii')
  
            # send data to client
            c.send(data) 
            
            tsPrint("Data sent:" + str(data))
            
        except Exception as e:

            tsPrint("An exception occurred: " + str(e))
            break
  
    # connection closed 
    c.close() 
    
    tsPrint("Connection closed")
  
  
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
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        tsPrint('Connected to :' + addr[0] + ':' + str(addr[1])) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
