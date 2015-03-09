'''
Created on Mar 8, 2015

@author: Kevin
'''
import server
import client
import threading

myClient = client()
myServer = server()

t = threading.Thread(target=myClient.listenTerminal)
t.daemon = True
t.start()

c = threading.Thread(target=myServer.update)
c.daemon = True
c.start()

