'''
Created on Apr 10, 2015

@author: Kevin
'''

import sys, math

class Node:
    database = {}
    fingerTable = {}
    key = 0
    bestValue = 0
    
    def __init__(self, key):
        self.key = key
        for i in range (0, 7):
            self.fingerTable[i] = math.pow(2, i)
        
    def addValue(self, key, value):
        self.database[key] = value
        
    def returnValue(self, key):
        return self.database[key]
                             
    def removeValue(self, key):
        del self.database[key]
        
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
                    