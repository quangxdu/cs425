'''
Created on Mar 8, 2015

@author: Kevin
'''
#Main should be called with the IP Address of the local host and the port it listens to
#Example:
#>> python main.py 192.168.101.70 5000
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

myServer.setClient(myClient)

#Continually loop and listen to the terminal
while True:
    n = raw_input('What message do you want to send? \n')
    message = n.split()
    if len(message) > 0:
        if(message[0] ==  "send"):
            myClient.addPacket(message[1], int(message[-1]))
        elif(message[0] == "q"):
            myServer.quit()
            sys.exit()
        elif((message[0] == "get") and (message[-1] == "2")):
            sys.stdout.write(myServer.returnValue(message[1])+"\n")
        elif(message[0] =="show-all"):
            for x in myServer.database:
                print x+": "+myServer.returnValue(x)+" \n"
        elif(message[0] == "delay"):
            myClient.addPacket(message[1], 5555,1)
        else:
            myClient.addPacket(n, 5005)

