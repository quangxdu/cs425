'''
Created on Mar 8, 2015

@author: Kevin
'''
import server
import client
import threading
import queue

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

