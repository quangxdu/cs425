'''
Created on Mar 8, 2015

@author: Kevin
'''
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
    
#Jump table for consistency model
model = {  1 : linear,
           2 : seq,
           3 : eventual1,
           4 : eventual2,
}
   
#Set up client ready to send to each server    
myClient = client.Client(sys.argv[1]);
t = threading.Thread(target=myClient.waitQueue)
t.daemon = True
t.start()

#Listen to designated central port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (sys.argv[1], 5005)
s.bind(server_address)

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
 