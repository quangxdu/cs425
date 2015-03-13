'''
Created on Mar 8, 2015

@author: Kevin
Indentations are 4 spaces wide
'''
#!/usr/bin/env python

import sys, socket

class PackStruct:
    pass

class Client:
    def __init__(self):
        pass
    
    def addPacket(self, msg, dest):
        packet = PackStruct()
        packet.message = msg
        packet.dest = dest

        UDP_PORT = 31337

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((packet.dest, UDP_PORT))
        s.send(packet.message)
        s.close()
        
