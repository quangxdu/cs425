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
	findCounter = 0
	addCounter = 0
		
	def __init__(self):
		for i in range(0, 256):
			self.NodeList[i] = None
		Node0 = nodes.node(0); Node0.database = {};
		newKeys = {}
		for i in range (0, 256):
			newKeys[i] = i
		Node0.addNodeKeys(1, newKeys)
		self.addCounter += 1
		Node0.setCoordinator(self)
		self.addCounter += 1
		self.NodeList[0] = Node0
		self.updateFingerTable()
		self.addCounter += 1

	def returnFirst(self):
		return self.NodeList[0]
	
	#Used by nodes to place a return value into the queue
	def returnValueToCoordinator(self, returnValue):
		self.returnQueue.put(returnValue)
	
	#Used by coordinator to get the return value
	def getReturnFromQueue(self):
		return self.returnQueue.get()
	
	def removeNode(self, num):
		#Find next node
		prevNode = self.nextNode(num)
		#Grab the tail of the current node being removed
		tail = self.NodeList[num].getTail()
		#Iterate through the current node and pick up all the keys
		removedKeys = self.NodeList[num].rmAllNodeKeys()
			#self.NodeList[num].addCmd(CmdStruct("rmAllNodeKeys"))
			#removedKeys = self.getReturnFromQueue()
		prevNode.addOldNodeKeys(tail, removedKeys)
			#cmd1 = CmdStruct("addNodeKeys", tail, removedKeys)
			#prevNode.addCmd(cmd1)
		self.NodeList[num] = None
		self.updateFingerTable()
		
	def addNode(self, num):
		prevNode = self.nextNode(num)
		#Find the tail of the previous node. This is the tail of the new node being added
		tail = prevNode.getTail();
		self.addCounter += 1
		#Create the new node
		newNode = nodes.node(num); newNode.database = {};
		newNode.setCoordinator(self)
		self.addCounter += 1
#		c = threading.Thread(target=newNode.checkQueue)
#		c.daemon = True
#		c.start()
		#Grab keys from the previous node
		removedKeys = prevNode.rmNodeKeys(num)
		self.addCounter += 1
		#cmd1 = CmdStruct("rmNodeKeys", num)
			#prevNode.addCmd(cmd1)
			#removedKeys = self.getReturnFromQueue()
		newNode.addNodeKeys(tail, removedKeys)
		self.addCounter += 1
		#Insert removed keys into our new node
		#cmd2 = CmdStruct("addNodeKeys", tail, removedKeys)
		#newNode.addCmd(cmd2)
		self.NodeList[num] = newNode
		self.updateFingerTable()
#		t1 = threading.Thread(target = newNode.checkQueue())
#		t1.daemon = True
#		t1.start
		return newNode
		
	def updateFingerTable(self):
		#Update finger tables
		for i in range(0,256):
			if(self.NodeList[i] is not None):
				tempdict = {};
				self.addCounter += 1
				for j in range(0,8):
					tempdict[j] = self.nextNode((i + math.pow(2,j)-1) %256).head
				self.NodeList[i].setFingerTable(tempdict)
		
	def findKey(self, num, key):
		self.findCounter += 1
		return self.NodeList[num].lookUp(key)
		
	def printAdd(self):
		print str(self.addCounter)
		
	def printFind(self):
		print str(self.findCounter)
		
	def show(self, num):
			#CmdStruct(self.show,num)
		if(self.NodeList[num] is not None):
			return self.NodeList[num].show()
		if(self.NodeList[num] is None):
			return None

	def showAll(self):
		s = ""
		for i in range(0,256):
			if(self.NodeList[i] is not None):
				s += self.show(i)
		return s
				
		#print entire dictionary
	def nearestNode(self,num):
		i = num
		while True:
			if(self.NodeList[i] is not None):
				break
			i = i + 1
			i = i % 256
		return i
	
	def nextNode(self,num):
		i = num + 1
		i = i%256
		while True:
			if(self.NodeList[i] is None): 
				pass
			else:
				temp = i
				break
			i = i + 1
			i = i%256
		return self.NodeList[temp]
