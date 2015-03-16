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
	def __init__(self, inputIP, port):
		self.ipAddress = inputIP
		self.port = port
	def update(self):
		while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (self.ipAddress,self.port)
            s.bind(server_address)
			connection, client_address = s.accept()
			data = s.recv(1024)
			connection.close()
			sys.stdout.write("Recieved: "+data+", System time is ---\n") #needs currTime
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

