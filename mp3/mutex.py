#
import sys,Queue,threading,node

cs_int = sys.argv[1]
next_req = sys.argv[2]
tot_exec_time = sys.argv[3]
option = sys.argv[4]

#initialize nodes
#1 2 3
#4 5 6
#7 8 9
q1 = Queue.Queue()
q2 = Queue.Queue()
q3 = Queue.Queue()
q4 = Queue.Queue()
q5 = Queue.Queue()
q6 = Queue.Queue()
q7 = Queue.Queue()
q8 = Queue.Queue()
q9 = Queue.Queue()

nodelist1= {q1,q2,q3,q4,q7}
nodelist2= {q2,q1,q3,q5,q8}
nodelist3= {q3,q1,q2,q6,q9}
nodelist4= {q4,q1,q7,q5,q6}
nodelist5= {q5,q4,q6,q2,q8}
nodelist6= {q6,q4,q5,q3,q9}
nodelist7= {q7,q8,q9,q1,q4}
nodelist8= {q8,q7,q9,q2,q5}
nodelist9= {q9,q7,q8,q3,q6}

n1 = node.node(nodelist1,cs_int,next_req)
n2 = node.node(nodelist2,cs_int,next_req)
n3 = node.node(nodelist3,cs_int,next_req)
n4 = node.node(nodelist4,cs_int,next_req)
n5 = node.node(nodelist5,cs_int,next_req)
n6 = node.node(nodelist6,cs_int,next_req)
n7 = node.node(nodelist7,cs_int,next_req)
n8 = node.node(nodelist8,cs_int,next_req)
n9 = node.node(nodelist9,cs_int,next_req)

nodelist = {n1,n2,n3,n4,n5,n6,n7,n8,n9}
