import nodes, coordinator, threading, sys

counter = 0
continue_looping = 1

#Check if the user wants writeback
writeback = 0
if len(sys.argv) > 2:
	if (sys.argv[1] == "-g"):
		outputfile = sys.argv[2]
		writeback = 1
		f = open(outputfile, 'w')
	
#Create new coordinator
coordinator = coordinator.Coordinator()
Node0 = coordinator.returnFirst()
t1 = threading.Thread(target = Node0.checkQueue)
t1.daemon = True
t1.start

while (continue_looping):
	n = raw_input('Type your command here: \n')
	message = n.split()
	if len(message) > 0:
		if(message[0] ==  "join"):
			coordinator.addNode(int(message[1]))
			sys.stdout.write("join complete")
			counter++
					
		if(message[0] == "find"):
			temp = coordinator.findKey(int(message[1]),int(message[2]))
			print temp
			sys.stdout.write("find complete")
			counter++
			
		if(message[0] == "leave"):
			coordinator.removeNode(int(message[1]))
			sys.stdout.write("leave complete")
			counter++

		if(message[0] == "show"):
			if(message[1] == "all"):
				if(writeback):
					f.write(coordinator.showAll())
				else
					coordinator.showAll()
			else:
				if(writeback):
					f.write(coordinator.show(int(message[1]))
				else
					coordinator.show(int(message[1]))
			sys.stdout.write("show complete")
		if(message[0] == "quit"):
			f.close()
			continue_looping = 0
			sys.stdout.write("quitting")

			
