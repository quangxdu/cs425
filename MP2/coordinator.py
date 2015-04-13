'''
@author Sam Du
'''
import sys, math, node, threading

class coordinator:
	NodeList = {}
		
	def removeNode(self, num):
		#Grab the tail of the current node being removed
		tail = self.nodelist[num].getTail()
		#Iterate through the current node and pick up all the keys
		removedKeys = self.nodeList[num].rmAllNodeKeys()
		'''
		TO IMPLEMENT: Find previous node in NodeList to collapse the keys into, call it prevNode
		'''
		prevNode.addNodeKeys(tail, removedKeys)
		del self.NodeList[num]
		
	def addNode(self, num):
		'''
		TO IMPLEMENT: Find previous node in NodeList to grab keys from, call it prevNode
		'''
		prevNode
		#Find the tail of the previous node. This is the tail of the new node being added
		tail = prevNode.getTail()
		#Create the new node
		newNode = node.Node(num)
		#Grab keys from the previous node
		removedKeys = prevNode.rmNodeKeys(num)
		#Insert removed keys into our new node
		newNode.addNodeKeys(tail, removedKeys)
		'''
		TO IMPLEMENT: Make a finger table
		'''
		self.NodeList[num] = newNode
		return newNode
		
	def findKey(self, num, key):
		#complicated-ish shit
	def show(self, num):
	def showAll:
		#print entire dictionary
	def nearestNode(self,num):
		i = num
		while True:
			if(nodeList[i] != 0):
				break
			i++
			i % 255
		return i
	'''
	main thread is coordinator, which reads from terminal for commands.
	each node is contained in the nodeList, which runs as a separate thread.
	node will contain keys.
	Initially we have node 0 which contains 0-255 keys 
	'''
	
	'''
	removeNode will contain functions
	moveKeysRM()
	deleteNode()
	
	addNode will contain functions
	createNode()
		create a node
		generate fingertable
	moveKeysADD()
	
	findKey will first go to node num, then call function lookup, which will call lookup(nkey) on new node.
	'''
#Create the first node with keys 0 to 255
Node0 = node.Node(0);
newKeys = {}
for i in range (0, 255)
	newKeys[i] = i
Node0.addNodeKeys(255, newKeys)
self.NodeList[0] = Node0
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
			c = threading.Thread(target=Node0.InsertFunctionHere)
			c.daemon = True
			c.start()
