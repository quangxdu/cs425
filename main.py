'''
Created on Mar 8, 2015

@author: Kevin
'''
import server
import client
import threading

def myClient(self):
	#setup connection to other 3 servers
	#while loop asking for packet info to send
	#create packet
	#insert into tail of queue with random delay
    pass

def myServer(self):
	#setup connections to other 3 clients
	#while loop receiving packet info
    pass

def myQueue(self):
	#check time, if head's packet time < currentTime send and inc head
    pass
	
t = threading.Thread(target=myClient.listenTerminal)
t.daemon = True
t.start()

c = threading.Thread(target=myServer.update)
c.daemon = True
c.start()

q = threading.Thread(target=myQueue.sendPacket)
q.daemon = True
q.start()

