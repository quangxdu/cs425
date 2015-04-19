import nodes, coordinator, threading, sys

	
#Create new coordinator
coordinator = coordinator.Coordinator()
Node0 = coordinator.returnFirst()
t1 = threading.Thread(target = Node0.checkQueue)
t1.daemon = True
t1.start

while True:
	n = raw_input('Type your command here: \n')
	message = n.split()
	if len(message) > 0:
		if(message[0] ==  "join"):
			coordinator.addNode(int(message[1]))
			sys.stdout.write("join complete")
			
		if(message[0] == "find"):
			temp = coordinator.findKey(int(message[1]),int(message[2]))
			print temp
			sys.stdout.write("find complete")
			
		if(message[0] == "leave"):
			coordinator.removeNode(int(message[1]))
			sys.stdout.write("leave complete")

		if(message[0] == "show"):
			if(message[1] == "all"):
				coordinator.showAll()	
			else:
				coordinator.show(int(message[1]))
			sys.stdout.write("show complete")
			

			
