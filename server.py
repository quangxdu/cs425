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
		
	def update(self):
		while True:
			data, address = self.s.recvfrom(1024)
			currTime = datetime.datetime.now()
			sys.stdout.write("Received: "+data+", System time is "+currTime.ctime()+" (Max Delay is 3 seconds)\n") #needs currTime
			message = data.split()
			if(message[0] == "delete"):
				del self.database[message[1]]
			elif(message[0] == "get"):
				value = self.database[message[1]]
				#Some method to send out return message
			elif(message[0] == "insert" or message[0] == "update"):
				self.database[message[1]] = message[2]
				#Some method to update other servers
	def returnTime(self):
		return datetime.datetime.now();
	def delayTime(self):
		return datetime.datetime.now() + datetime.timedelta(seconds = random.uniform(0,maxdelay));

