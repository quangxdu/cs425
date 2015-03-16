'''
Created on Mar 8, 2015

@author: Kevin
Indentations are 4 spaces wide
'''
#!/usr/bin/env python

import sys, socket, Queue, datetime, random

class PackStruct:
    def sendPacket(self, ipAddress, port, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(ipAddress, port)
        s.send(message)
        s.close()

class Client:

    ipAddress = "0"
    packetQueue = Queue.Queue(0)
    
    def __init__(self, inputIP):
        self.ipAddress = inputIP

    def waitQueue(self):
        #Check top value of queue for matching time
        while True:
            temp = Client.packetQueue.get()
            while True:
                if(temp.sendTime >= datetime.datetime.now()):
                    temp.sendPacket(self.ipAddress, temp.dest, temp.message)
                    break;

    def addPacket(self, msg, dest):
        packet = PackStruct()
        packet.message = msg
        packet.dest = dest
        currTime = datetime.datetime.now()
        packet.time = currTime
        delay = datetime.timedelta(seconds = random.uniform(0,3))
        packet.sendTime = currTime + delay
        packet.port = dest
        sys.stdout.write("Sent: "+msg+" to "+str(dest)+", System time is ---\n") #needs currTime
        Client.packetQueue.put(packet)
 
