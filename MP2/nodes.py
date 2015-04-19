'''
Created on Apr 10, 2015

@author: Kevin
'''

import sys, math, coordinator, Queue


class node:
    cmdQueue = Queue.Queue(0)
    database = {}
    coordinator
    fingerTable = {}
    head = 0
    tail = 0
    bestValue = 0
    
    def __init__(self, head):
        self.head = head
        self.tail = head
        
        '''
        TO IMPLEMENT: This is the function that will be spinning. It should
         continually check the queue and do things when a command is popped
         off the queue.
        '''
    def checkQueue(self):
        while True:
		 print "derp"
            n = self.cmdQueue.get()
            print "Node: Popped command from Coordinator off queue"
            if(n.cmd ==  "rmAllNodeKeys"):
                self.rmAllNodeKeys()
            elif(n.cmd ==  "rmNodeKeys"):
                self.rmNodeKeys(n.arg1)            
            elif(n.cmd ==  "addNodeKeys"):
                self.addsNodeKeys(n.arg1, n.arg2)
            elif(n.cmd == "show"):
                print "Node: Command recognized as show"
                self.show()

    #Used by coordinator to give a command to the node
    def addCmd(self, cmd):
        #Interpret cmd here
        print "Node: Entering add command, inserting into queue"
        self.cmdQueue.put(cmd)
        print "Node: Finished inserting into queue"
    
    #Used to return a value to the coordinator
    def returnValueToCoordinator(self, value):
        print "Sending return value"
        self.coordinator.returnValueToCoordinator(value)
               
    def addValue(self, key):
        self.database[key] = key
        
    def returnValue(self, key):
        self.coordinator.returnValueToCoordinator(self.database[key])
    
    def getTail(self):
        self.coordinator.returnValueToCoordinator(self.tail)
    
    def setFingerTable(self, table):
        self.fingerTable = table
    
    #rmNodeKeys takes in a new tail (smaller than self.head, greater than self.tail
    #and iterates through the database, removing keys and adding them to a new
    #temporary dictionary which it then returns. Also updates self.tail
    def rmNodeKeys(self, newTail):
        removedKeys = {}
        while self.tail != newTail:
            removedKeys[self.tail] = self.database[self.tail]
            del self.database[self.tail]
            self.tail = (self.tail + 1 ) % 256
        self.tail += 1
        self.coordinator.returnValueToCoordinator(removedKeys)
    
    #rmAllNodeKeys is called during removeNode and removes all keys, places them
    #in a temporary dictionary, and returns that dictionary. 
    def rmAllNodeKeys(self):
        removedKeys = {}
        for i in range(self.tail, self.head+1):
            removedKeys[i] = self.database[i]
            del self.database[i]
        self.coordinator.returnValueToCoordinator(removedKeys)
    
    #addNodeKeys takes in a new tail (smaller than self.head) and iterates
    #through the newKeys dictionary parameter, adding those keys to self.dictiona ry
    #and then updates self.tail. 
    def addNodeKeys(self, newTail, newKeys):
        i = newTail
        while (i != self.tail):

            self.database[i] = newKeys[i]
            i = (i + 1 ) % 256
        self.tail = newTail
    def initNode(self):
		self.database[0] = 0
		
    def setCoordinator(self, coord):
        self.coordinator = coord
        
    def lookUp(self, key):
        if key in self.database.values():
            return self.database[key]
        else:
            for i in range (0, 7):
                if key > self.fingerTable[i]:
                    break
                else:
                    bestValue = i
                return self.coordinator.lookUp(bestValue,key)

    def show(self):
        print self.head
        for key in self.database:
            print key ,":", self.database[int(key)]
