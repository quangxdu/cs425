'''
check argv
set up output socket for each server,
set up input socket for each server,
server multithread- recv from other servers
client multithread- take input and create packets to send to all 3 others
delay multithread- take created packets and send at correct time
'''

import datetime;

maxdelay = 3

def update(self):
	pass 			#Code for listening to a port


def returnTime():
	return datetime.datetime.now();
def delayTime():
	return datetime.datetime.now() + datetime.timedelta(seconds = random.uniform(0,maxdelay));

