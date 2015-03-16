'''
Created on Mar 8, 2015

@author: Kevin
'''
import server, client, threading, sys

myClient = client.Client(sys.argv[1]);
myServer = server.Server(sys.argv[1], sys.argv[2]);

t = threading.Thread(target=myClient.waitQueue)
t.daemon = True
t.start()

c = threading.Thread(target=myServer.update)
c.daemon = True
c.start()


while True:
    n = input('What message do you want to send? ')
    if(input == "quit"):
        break;
    message = n.split()
    if(message[0] ==  "send" and  message.len == 3):
        myClient.addPacket(message[1], message[-1])     #Need to modify message[1]

