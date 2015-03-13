'''
check argv
set up output socket for each server,
set up input socket for each server,
server multithread- recv from other servers
client multithread- take input and create packets to send to all 3 others
delay multithread- take created packets and send at correct time
'''

import datetime, random, socket

maxdelay = 3

def update(self):
	while True
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		data = s.recv(1024)
		s.close()
		print "Received data: ", data, " System time is: ", returnTime();


def returnTime():
	return datetime.datetime.now();
def delayTime():
	return datetime.datetime.now() + datetime.timedelta(seconds = random.uniform(0,maxdelay));

