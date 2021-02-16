
# import socket programming library 

from src.user import *
from src.channel import *
from src.channels import *

global htConnection
online_users = 0
MAX_USERS = 50
isRunning = True

users = dict()
channels = [Channel(Channels.GENERAL.value), Channel(Channels.GUILD.value)]

def removeUser(user):
    global online_users

    users.pop(user)
    online_users -= 1

    del user

    tsPrint("Users online: " + str(online_users))

def handle_connections(s):
    global online_users

    # a forever loop until client wants to exit 
    while isRunning: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        tsPrint('Connected to :' + addr[0] + ':' + str(addr[1])) 
        
        newUser = User(c, removeUser)
        
        idChannel = channels[Channels.GENERAL.value].attach(newUser)
        newUser.channels.append(idChannel)
        now = datetime.datetime.now()
                
        data = "Hello I am the server. Time: " + now.strftime("%H:%M:%S %d/%m/%Y")

        newUser.outputQ.append(data)
        
        users[newUser] = -1

        online_users += 1

        tsPrint("Users online: " + str(online_users))
        

def Main(): 

    host = "" 
  
    port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(MAX_USERS) 
    print("socket is listening")

    # Start a new thread to handle new connections
    htConnection = start_new_thread(handle_connections, (s,))

    while True:

        for i in users:

            # Check pending outgoing data to send to user i            
            while i.outputQ:
                msg = i.outputQ.popleft()
                i.socket.send(msg.encode('ascii'))

        for i in channels:

            # Check if channels has pending data to notify
            i.notify()

                
        time.sleep(0.5)
    

    isRunning = False 
    s.close() 
  
if __name__ == '__main__': 
    Main() 
