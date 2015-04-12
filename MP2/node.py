'''
Created on Apr 10, 2015

@author: Kevin
'''

import sys, math, coordinator

class Node:
    database = {}
    coordinator
    fingerTable = {}
    head = 0
    tail = 0
    bestValue = 0
    
    def __init__(self, head):
        self.head = head
        
    def addValue(self, key, value):
        self.database[key] = value
        
    def returnValue(self, key):
        return self.database[key]
                             
    def removeValue(self, key):
        del self.database[key]
        
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
           # return requestCoordinator    Request coordinator to lookUp on closer 
                    