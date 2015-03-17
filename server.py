'''
check argv
set up output socket for each server,
set up input socket for each server,
server multithread- recv from other servers
client multithread- take input and create packets to send to all 3 others
delay multithread- take created packets and send at correct time
'''

import datetime, random, socket, client, sys

maxdelay = 3

#The server holds the key-value database and handles incoming
#packets. It takes in the local host IP address and the port
#it should be listening to.
class Server:
	database = {}
	port = "0"
	ipAddress = "0"
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client
		
	def __init__(self, inputIP, port):
		self.ipAddress = inputIP
		self.port = port
		server_address = (self.ipAddress, int(self.port))
		self.s.bind(server_address)
		
	#The update function spins forever, listening at the specified
	#port until it sees a packet. It then processes the packet
	#based on the contents and prints out the current time and
	#the received data
	def update(self):
		while True:
			data, address = self.s.recvfrom(1024)
			currTime = datetime.datetime.now()
			message = data.split()
			sys.stdout.write("Received: "+data+", System time is "+currTime.ctime()+" (Max Delay is 3 seconds)\n")
			#Perform operations
			if message[0] is "delete":
				del self.database[message[1]]
				sys.stdout.write("Delete recieved\n")
			elif message[0] is "insert" or message[0] is "update":
				sys.stdout.write("Recieved insert)\n")
				self.database[message[1]] = message[2]
				self.client.addPacket("ack", 5005)
			elif message[0] is "get":
				sys.stdout.write("Recieved get\n")
				sys.stdout.write("Get: "+self.database[message[1]]+"\n")
				self.client.addPacket("ack", 5005)
	
	def returnValue(self, key):
		return self.database[key]
	#Sets up the client for returning ack messages
	def setClient(self, client):
		self.client = client
	#Helper function that returns the current time
	def returnTime(self):
		return datetime.datetime.now();
	#Helper function that adds a random delay
	def delayTime(self):
		return datetime.datetime.now() + datetime.timedelta(seconds = random.uniform(0,maxdelay));
	#Cleanup function that is called at the end of main to close sockets
	def quit(self):
		self.s.close()

