'''
@author Sam Du
'''
import sys, math, node, threading, Queue
import cmd

class CmdStruct:
	cmd
	arg1 = 0
	arg2 = 0
	def __init__(self, cmd):
		self.cmd = cmd


class Coordinator:
	NodeList = {}
	returnQueue = Queue.Queue(0)
		
	def __init__(self):
		for i in range(0, 255):
			self.NodeList[i] = 0
		t1 = threading.Thread(target = node.Node, args = [0])
		t1.daemon = True
		t1.start()
		Node0 = node.Node(0)
		newKeys = {}
		for i in range (0, 255):
			newKeys[i] = i
		Node0.addNodeKeys(1, newKeys)
		Node0.setCoordinator(self)
		self.NodeList[0] = Node0
		
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
		removedKeys = self.nodeList[num].addCmd(CmdStruct("rmAllNodeKeys"))
		cmd1 = CmdStruct("addNodeKeys")
		cmd1.arg1 = tail
		cmd1.arg2 = removedKeys
		prevNode.addCmd(cmd1)
		self.NodeList[num] = 0
		
	def addNode(self, num):
		prevNode = self.Coordinator.prevNode(num)
		#Find the tail of the previous node. This is the tail of the new node being added
		tail = prevNode.getTail()
		#Create the new node
		newNode = node.Node(num)
		c = threading.Thread(target=newNode.InsertFunctionHere)
		c.daemon = True
		c.start()
		#Grab keys from the previous node
		removedKeys = prevNode.rmNodeKeys(num)
		#Insert removed keys into our new node
		newNode.addNodeKeys(tail, removedKeys)
		newNode.setCoordinator(self)
		self.NodeList[num] = newNode
		#Update finger tables
		for i in range(0,255):
			if(self.NodeList != 0):
				tempdict = {}
				for j in range(0,7):
					tempdict[j] = self.nearestNode(num + math.pow(2,j))
				self.Nodelist[i].setFingerTable(tempdict)
		return newNode
		
	def findKey(self, num, key):
		#complicated-ish shit
	def show(self, num):
	def showAll(self):
		#print entire dictionary
	def nearestNode(self,num):
		i = num
		while True:
			if(self.NodeList[i] != 0):
				break
			i++
			i = i % 256
		return i
	
	def nextNode(self,num)
		i = num - 1
		i = i%256
		temp = 0
		while True:
			if(self.NodeList[i] != 0):
				if(self.NodeList[i].head == num)
					break
				temp = i
				i--
				i = i%256
		return temp
	
#Create new coordinator
coordinator = coordinator.Coordinator()
#Start up new thread for the first node
'''
TO IMPLEMENT: Make looping thread function and replace InsertFunctionHere
'''
c = threading.Thread(target=Node0.InsertFunctionHere)
c.daemon = True
c.start()


while True:
	n = raw_input('Type your command here: \n')
	message = n.split()
	if len(message) > 0:
		if(message[0] ==  "join"):
			coordinator.addNode(message[1])
			'''
			TO IMPLEMENT: InsertFunctionHere
			'''
			
			sys.stdout.write("join complete")
			
		if(message[0] == "find"):
			coordinator.findKey(message[1],message[2])
			sys.stdout.write("find complete")
			
		if(message[0] == "leave"):
			coordinator.removeNode(message[1])
			sys.stdout.write("leave complete")

		if(message[0] == "show"):
			if(message[1] == "all"):
				pass
			sys.stdout.write("show complete")

			
