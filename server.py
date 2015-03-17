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
	def returnTime(self):
		return datetime.datetime.now();
	def delayTime(self):
		return datetime.datetime.now() + datetime.timedelta(seconds = random.uniform(0,maxdelay));

