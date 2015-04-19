'''
Created on Apr 10, 2015

@author: Kevin
'''

import sys, math, coordinator, Queue

class Node:
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
        return self.cmdQueue.get()
    
    #Used by coordinator to give a command to the node
    def addCmd(self, cmd):
        #Interpret cmd here
        self.cmdQueue.put(cmd)
    
    #Used to return a value to the coordinator
    def returnValueToCoordinator(self, value):
        self.coordinator.returnValueToCoordinator(value)
               
    def addValue(self, key):
        self.database[key] = key
        
    def returnValue(self, key):
        self.coordinator.returnValueToCoordinator(self.database[key])
    
    def getTail(self):
        self.coordinator.returnValueToCoordinator(self.tail)
    
    def setFingerTable(self, table):
        self.fingerTable = table
    
    #rmNodeKeys takes in a new tail (greater than self.head, smaller than self.tail
    #and iterates through the database, removing keys and adding them to a new
    #temporary dictionary which it then returns. Also updates self.tail
    def rmNodeKeys(self, newTail):
        removedKeys = {}
        for i in range(newTail, self.tail):
            removedKeys[i] = self.database[i]
            del self.database[i]
        self.tail = (newTail-1)
        return removedKeys
    
    #rmAllNodeKeys is called during removeNode and removes all keys, places them
    #in a temporary dictionary, and returns that dictionary. 
    def rmAllNodeKeys(self):
        removedKeys = {}
        for i in range(self.head, self.tail):
            removedKeys[i] = self.database[i]
            del self.database[i]
        return removedKeys
    
    #addNodeKeys takes in a new tail (greater than self.head and self.tail) and iterates
    #through the newKeys dictionary parameter, adding those keys to self.dictionary
    #and then updates self.tail. 
    def addNodeKeys(self, newTail, newKeys):
        for i in range(self.tail, newTail):
            self.database[i] = newKeys[i]
        self.tail = newTail
        
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
    