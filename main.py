'''
Created on Mar 8, 2015

@author: Kevin
'''
import server
import client
import threading
import queue



def myClient():
	#setup connection to other 3 servers
	#while loop asking for packet info to send
	#create packet
	#insert into tail of queue with random delay
    pass

def myServer():
	#setup connections to other 3 clients
	#while loop receiving packet info
	#print info
    pass

def myQueue():
	#check time, if head's packet time < currentTime send and inc head
    pass
#loop

t = threading.Thread(target=myClient.listenTerminal)
myClient = client();
myServer = server();

t = threading.Thread(target=myClient.waitQueue)
t.daemon = True
t.start()

c = threading.Thread(target=myServer.update)
c.daemon = True
c.start()


while True:
	n = input('what message do you want to send?')
	if(input == "quit"):
		break;
	message = n.split()
	if(message[0] ==  "send" and  message.len == 3):
        myClient.addpacket(message[1], message[-1])

