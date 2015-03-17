'''
Created on Mar 8, 2015

@author: Kevin
'''
#Central should be called with the IP Address of the local host
#Example:
#>> python central.py 192.168.101.70
import server, client, threading, sys, socket, Queue
from curses.ascii import ACK

class PackStruct:
    def sendPacket(self, ipAddress, port, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(message, (ipAddress, port))
        s.close()

#This function loops and listens to port 5005 for commands
#and then passes it to one of the consistency functions to
#send out the messages in the correct order 
def masterListen():
    while True:
        data, address = s.recvfrom(1024)
        sys.stdout.write("Received: "+data+"\n")
        
        message = data.split()
        if(message[0] is "ack"):
            ACK = ACK-1
        #Check if command is delete
        elif(message[0] == "delete"):
            #Send delete signal to each server
            temp = PackStruct()
            temp.sendPacket(ipAddress, 5000, data)
            temp.sendPacket(ipAddress, 5001, data)
            temp.sendPacket(ipAddress, 5002, data)
            temp.sendPacket(ipAddress, 5003, data)
            #Else choose consistency model
        else:
            addPacket(data, address)
    
def sendMsg():
    while True:
    #Check top value of queue for matching time
        if(ACK <= 0):
            temp = packetQueue.get()
            n = temp.message.split()
            if(n[0] == "get" and n[-1] == "1"):
                temp.sendPacket(ipAddress, temp.addresss, temp.message)
                ACK = 1
            elif(n[0] == "get" and n[-1] == "2"):
                ACK = 0
            else:
                temp.sendPacket(ipAddress, 5000, temp.message)
                temp.sendPacket(ipAddress, 5001, temp.message)
                temp.sendPacket(ipAddress, 5002, temp.message)
                temp.sendPacket(ipAddress, 5003, temp.message)
                ACK = 4

def addPacket(msg, address):
    packet = PackStruct()
    packet.message = msg
    packet.address = address
    packetQueue.put(packet)
    
global ACK
ACK = 4
data = "0"

packetQueue = Queue.Queue(0)

#Set up client ready to send to each server    
ipAddress = sys.argv[1]
t = threading.Thread(target=sendMsg)
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
    n = raw_input('Type quit to exit\n')
    msg = n.split()
    if len(msg) > 0:
        if(msg[0] == "q"):
            s.close()
            sys.exit()
 