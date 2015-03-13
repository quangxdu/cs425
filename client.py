'''
Created on Mar 8, 2015

@author: Kevin
Indentations are 4 spaces wide
'''
#!/usr/bin/env python

import sys, socket, queue

#Global variables
packetQueue = queue()
UDP_PORT = 31337

class PackStruct:
    pass

class Client:
    def __init__(self):
        pass
    
    def listenToTerminal(self):
        #Check top value of queue for matching time
        pass
    
    def addPacket(self, msg, dest):
        packet = PackStruct()
        packet.message = msg
        packet.dest = dest
        packetQueue.put(packet)

    def sendPacket(self, packet):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((packet.dest, UDP_PORT))
        s.send(packet.message)
        s.close()
        
