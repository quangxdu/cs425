'''
Created on Mar 8, 2015

@author: Kevin
'''
import server, client, threading, sys

myServer = server.Server(sys.argv[1], sys.argv[2]);
c = threading.Thread(target=myServer.update)
c.daemon = True
c.start()

myClient = client.Client(sys.argv[1]);
t = threading.Thread(target=myClient.waitQueue)
t.daemon = True
t.start()

myServer.getClient(myClient)

while True:
    n = raw_input('What message do you want to send? ')
    message = n.split()
    if len(message) > 0:
        if(message[0] ==  "send"):
            myClient.addPacket(message[1], int(message[-1]))
        elif(message[0] == "quit"):
            sys.exit();     #Need to modify message[1]
        elif(message[0] == "delete"):
            del database[message[1]]
        elif(message[0] == "get"):
            value = database[message[1]]
            myClient.addPacket(message[1], message[2])
        elif(message[0] == "insert" or message[0] == "update"):
            database[message[1]] = message[2]
            #Some method to update other servers

