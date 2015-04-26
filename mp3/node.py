'''
Created on Apr 25, 2015

@author: Kevin
'''

import  Queue,Thread
from cs425.mp3.mutex import cs_int

class node(Thread):
    neighbors = []
    cs_int = 0
    next_req = 0
    

    
    def __init__(self, node_num, cs_int, next_req):
        for i in range(0, 5):
            self.neighbors.append(node_num[i])
        self.cs_int = cs_int
        self.next_req = next_req
        
    def run(self):
        while(True):
