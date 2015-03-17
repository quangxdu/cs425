'''
Created on Mar 8, 2015

@author: Kevin
'''
import server, client, threading, sys

#Create a new server and make a new thread to
#listen to the specified port
myServer = server.Server(sys.argv[1], sys.argv[2]);
c = threading.Thread(target=myServer.update)
c.daemon = True
c.start()

#Create a new client and make a new thread to
#send out new packets when they are made
myClient = client.Client(sys.argv[1]);
t = threading.Thread(target=myClient.waitQueue)
t.daemon = True
t.start()

#Continually loop and listen to the terminal
while True:
    n = raw_input('What message do you want to send? ')
    message = n.split()
    if len(message) > 0:
        if(message[0] ==  "send"):
            myClient.addPacket(message[1], int(message[-1]))
        elif(message[0] == "quit"):
            myClient.quit()
            myServer.quit()
            sys.exit()
        elif(message[0] == "delete"):
            #
        elif(message[0] == "get"):
            #
        elif(message[0] == "insert" or message[0] == "update"):
            #

