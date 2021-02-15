import socket
import time

#create an INET, STREAMing socket (IPv4, TCP/IP)
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('Socket Created')

ROBOT_IP= "127.0.0.1"
ROBOT_PORT = 80
#Connect the socket object to the robot using IP address (string) and port (int)
client.connect((ROBOT_IP,ROBOT_PORT))

print('Socket Connected to ' + ROBOT_IP )
#Read the response sent by robot upon connecting
msg = client.recv(1024).decode('ascii')
print(msg)

# Add ASCII NULL character at the end of the cmd string
try:
    client.send(bytes('Encantado, yo el cliente\0','ascii'))
    time.sleep(3)
    print(msg)
    
except socket.error:
    print('Failed to send data')



#Disconnect from the robot and close the socket object
client.close()
#sys.exit()