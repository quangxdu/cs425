'''
Created on Mar 8, 2015

@author: Kevin
Indentations are 4 spaces wide
'''
#!/usr/bin/env python

import sys, socket, threading

class PackStruct:
    pass

class Client:
    def __init__(self):
        pass
    
    def listenTerminal(self):
        if len(sys.argv) is not 3:
            print "Not enough arguments! Try again!"
            return False
    
        packet = PackStruct()
        packet.message = sys.argv[1]
        packet.dest = sys.argv[2]

        UDP_PORT = 31337

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((packet.dest, UDP_PORT))
        s.send(packet.message)
        s.close()
        
    
    my_thread = threading.Thread(target=listenTerminal)
    my_thread.start()
