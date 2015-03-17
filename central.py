'''
Created on Mar 8, 2015

@author: Kevin
'''
#Central should be called with the IP Address of the local host
#Example:
#>> python central.py 192.168.101.70
import server, client, threading, sys, socket
       
#--------------TO IMPLEMENT: THE FOUR CONSISTENCY MODELS-------------------
def linear():
    myClient.addPacket(data, 5000)
    myClient.addPacket(data, 5001)
    myClient.addPacket(data, 5002)
    myClient.addPacket(data, 5003)

def seq():
    myClient.addPacket(data, 5000)
    myClient.addPacket(data, 5001)
    myClient.addPacket(data, 5002)
    myClient.addPacket(data, 5003)

def eventual1():
    myClient.addPacket(data, 5000)
    myClient.addPacket(data, 5001)
    myClient.addPacket(data, 5002)
    myClient.addPacket(data, 5003)

def eventual2():
    myClient.addPacket(data, 5000)
    myClient.addPacket(data, 5001)
    myClient.addPacket(data, 5002)
    myClient.addPacket(data, 5003)

#This function loops and listens to port 5005 for commands
#and then passes it to one of the consistency functions to
#send out the messages in the correct order 
def masterListen():
    while True:
        data, address = s.recvfrom(1024)
        message = data.split()
        #Check if command is delete
        if message[0] is "delete":
            #Send delete signal to each server
            myClient.addPacket(data, 5000)
            myClient.addPacket(data, 5001)
            myClient.addPacket(data, 5002)
            myClient.addPacket(data, 5003)
            #Else choose consistency model
        else:
            model[message[-1]]()
    
#Jump table for consistency model
model = {  1 : linear,
           2 : seq,
           3 : eventual1,
           4 : eventual2,
}
data = "0"

#Set up client ready to send to each server    
myClient = client.Client(sys.argv[1]);
t = threading.Thread(target=myClient.waitQueue)
t.daemon = True
t.start()

#Listen to designated central port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (sys.argv[1], 5005)
s.bind(server_address)

#Start listening to port 5005
t = threading.Thread(target=masterListen)
t.daemon = True
t.start()

while True:
    n = raw_input('Type quit to exit/n')
    msg = n.split()
    if len(msg) > 0:
        if(msg[0] == "quit"):
            myClient.quit()
            s.close()
            sys.exit()
 