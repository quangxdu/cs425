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
			sys.stdout.write("Received: "+data+", System time is "+currTime.ctime()+" (Max Delay is 3 seconds)\n")
			message = data.split()
			if message[0] is "delete":
				del self.database[message[1]]
			elif message[0] is "insert" or message[0] is "update":
				self.database[message[1]] = message[2]
			elif message[0] is "get":
				sys.stdout.write("Get: "+self.database[message[1]]+"\n")
				#This method is probably not the correct implementation of get -- it is simply a placeholder
			
	#Helper function that returns the current time
	def returnTime(self):
		return datetime.datetime.now();
	#Helper function that adds a random delay
	def delayTime(self):
		return datetime.datetime.now() + datetime.timedelta(seconds = random.uniform(0,maxdelay));
	#Cleanup function that is called at the end of main to close sockets
	def quit(self):
		self.s.close()

