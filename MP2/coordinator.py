'''
@author Sam Du
'''
import sys, math, nodes, threading, Queue
import cmd

class CmdStruct:
	cmd
	arg1 = 0
	arg2 = 0
	def __init__(self, cmd,arg1 = 0, arg2 = 0):
		self.cmd = cmd
		self.arg1 = arg1
		self.arg2 = arg2


class Coordinator:
	NodeList = {}
	returnQueue = Queue.Queue(0)
		
	def __init__(self):
		for i in range(0, 256):
			self.NodeList[i] = 0
		Node0 = nodes.node(0)
		newKeys = {}
		for i in range (0, 256):
			newKeys[i] = i
		Node0.addNodeKeys(1, newKeys)
		Node0.setCoordinator(self)
		self.NodeList[0] = Node0		
		t1 = threading.Thread(target=Node0.checkQueue())
		t1.daemon = True
		t1.start()
		
	#Used by nodes to place a return value into the queue
	def returnValueToCoordinator(self, returnValue):
		self.returnQueue.put(returnValue)
	
	#Used by coordinator to get the return value
	def getReturnFromQueue(self):
		return self.returnQueue.get()
	
	def removeNode(self, num):
		#Find previous node
		prevNode = self.Coordinator.prevNode(num)
		#Grab the tail of the current node being removed
		tail = self.nodelist[num].getTail()
		#Iterate through the current node and pick up all the keys
		self.nodeList[num].addCmd(CmdStruct("rmAllNodeKeys"))
		removedKeys = self.getReturnFromQueue()
		cmd1 = CmdStruct("addNodeKeys", tail, removedKeys)
		prevNode.addCmd(cmd1)
		self.updateFingerTable(num)
		self.NodeList[num] = 0
		
	def addNode(self, num):
		prevNode = self.Coordinator.prevNode(num)
		#Find the tail of the previous node. This is the tail of the new node being added
		tail = prevNode.getTail()
		#Create the new node
		newNode = node.Node(num)
		newNode.setCoordinator(self)
		c = threading.Thread(target=newNode.checkQueue())
		c.daemon = True
		c.start()
		#Grab keys from the previous node
		cmd1 = CmdStruct("rmNodeKeys", num)
		prevNode.addCmd(cmd1)
		removedKeys = self.getReturnFromQueue()
		#Insert removed keys into our new node
		cmd2 = CmdStruct("addNodeKeys", tail, removedKeys)
		newNode.addCmd(cmd2)
		self.NodeList[num] = newNode
		self.updateFingerTable(num)
		return newNode
		
	def updateFingerTable(self, num):
		#Update finger tables
		for i in range(0,256):
			if(self.NodeList != 0):
				tempdict = {}
				for j in range(0,7):
					tempdict[j] = self.nearestNode(num + math.pow(2,j))
				self.Nodelist[i].setFingerTable(tempdict)
		
	def findKey(self, num, key):
		return self.NodeList[num].lookUp(key)
		
	def show(self, num):
		CmdStruct(self.show,num)
		self.Nodelist[num].show()
		
	def showAll(self):
		for i in range(0,256):
			if(self.NodeList[i] != 0):
				self.show(i)
				
		#print entire dictionary
	def nearestNode(self,num):
		i = num
		while True:
			if(self.NodeList[i] != 0):
				break
			i = i + 1
			i = i % 256
		return i
	
	def nextNode(self,num):
		i = num - 1
		i = i%256
		temp = 0
		while True:
			if(self.NodeList[i] != 0):
				if(self.NodeList[i].head == num):
					break
				temp = i
				i = i - 1
				i = i%256
		return temp
