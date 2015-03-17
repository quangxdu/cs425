'''
Created on Mar 8, 2015

@author: Kevin
Indentations are 4 spaces wide
'''
#!/usr/bin/env python

import sys, socket, Queue, datetime, random

#This is a struct that holds a packet and its time to send
#while it is sitting in the queue. It will contain both the
#IP address and the port number of the destination
class PackStruct:
    def sendPacket(self, ipAddress, port, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(message, (ipAddress, port))
        s.close()

#This is the client class. It takes an input IP address which
#is the IP address of the local host
class Client:
    ipAddress = "0"
    packetQueue = Queue.Queue(0)
    
    def __init__(self, inputIP):
        self.ipAddress = inputIP
        
    #The waitQueue function will spin
    #forever until main quits as it continually checks the top 
    #of the packet queue to see if it is time to send out
    #each packet. 
    def waitQueue(self):
        #Check top value of queue for matching time
        while True:
            temp = Client.packetQueue.get()
            while True:
                if(temp.sendTime <= datetime.datetime.now()):
                    if(temp.delay == 0):
                        temp.sendPacket(self.ipAddress, temp.dest, temp.message)
                    break;
            
    #This function will add a packet to the queue after randomly 
    #adding in a delay time. It will also print out the sending
    #time, the message, and the destination
    def addPacket(self, msg, dest, delay =0):
        packet = PackStruct()
        packet.message = msg
        packet.dest = dest
        packet.delay = delay
        currTime = datetime.datetime.now()
        packet.time = currTime
        randtemp = random.uniform(0,3)
        if(delay == 1):
            randtemp = msg
        packet.sendTime = currTime + datetime.timedelta(seconds=randtemp)
        sys.stdout.write("Sent: "+msg+" to "+str(dest)+", System time is +" +currTime.ctime()+"\n")
        Client.packetQueue.put(packet)

