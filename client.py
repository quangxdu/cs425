'''
Created on Mar 8, 2015

@author: Kevin
Indentations are 4 spaces wide
'''
#!/usr/bin/env python

import sys, socket, queue, datetime, random

class PackStruct:
    pass

class Client:
    #Object variables
    packetQueue = queue()
    ipAddress = "0"
    
    def __init__(self, inputIP):
        ipAddress = inputIP
        pass
    
    def waitQueue(self):
        #Check top value of queue for matching time
        pass
    
    def addPacket(self, msg, dest):
        packet = PackStruct()
        packet.message = msg
        packet.dest = dest
		currTime = datetime.datetime.now()
		packet.time = currTime
		delay = datetime.timedelta(seconds = random.uniform(0,3))
		packet.sendTime = currTime + delay
        packet.port = dest

        packetQueue.put(packet)

    def sendPacket(self, packet):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ipAddress, packet.port))
        s.send(packet.message)
        s.close()
        
