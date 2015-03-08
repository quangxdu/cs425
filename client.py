'''
Created on Mar 8, 2015

@author: Kevin
Indentations are 4 spaces wide
'''
#!/usr/bin/env python

import sys, socket

class PackStruct:
    pass

if len(sys.argv) is not 3:
    print "Not enough arguments! Try again!"
    
packet = PackStruct()
packet.message = sys.argv[1]
packet.dest = sys.argv[2]

UDP_PORT = 31337
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((packet.dest, UDP_PORT))
s.send(packet.message)
s.close()