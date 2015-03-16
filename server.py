'''
check argv
set up output socket for each server,
set up input socket for each server,
server multithread- recv from other servers
client multithread- take input and create packets to send to all 3 others
delay multithread- take created packets and send at correct time
'''

import datetime, random, socket, client

maxdelay = 3

class Server:
	database = {}
	def update(self, ipAddr, port):
		while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ipAddr, port))
			data = s.recv(1024)
			s.close()
			print "Received data: ", data, " System time is: ", Server.returnTime()
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

