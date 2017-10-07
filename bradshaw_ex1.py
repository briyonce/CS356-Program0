import socket
import random
import sys

DEBUG = 0

#step a
psock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create new intermediate socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create initial socket
if (DEBUG):
	print client_sock.getsockname()
client_sock.connect(('128.83.144.56', 35603)) #connect to server
addr = client_sock.getsockname()
if (DEBUG):
	print addr
#step b
psock.bind((addr[0],0)) #bind psock to whichever address client_sock connected to
#step c
addr = psock.getsockname()
print ("Address: " + str(addr[0]) + " Port: " + str(addr[1]))
port = addr[1]
#step d
psock.listen(5)
usernum = random.randint(1,9001)
#step e
req_string = "ex1 128.83.144.56-35603 " + str(addr[0]) + "-" + str(addr[1]) + " " + str(usernum) + " B.M.Bradshaw\n"
if(DEBUG):
	print req_string

#step f
client_sock.send(req_string)
reply1 = client_sock.recv(4096) #throwaway reply

#step g
reply2 = client_sock.recv(4096)
if(DEBUG):
	print reply2
reply2tok = reply2.split(" ")
if(DEBUG):
	print reply2tok

if(reply2tok[0] != "OK"):
	sys.exit("ACK ERROR")

servernum = int(reply2tok[3]) + 1

#step h
temp = (psock.accept()) 
newsock = temp[0] #accept returns (conn,address), where conn is a new sock object 
if (DEBUG):
	print newsock
	print newsock.getsockname()

#step i
reply = newsock.recv(4096)
if (DEBUG):
	print reply
replytok = reply.split(" ")
newservernum = int(replytok[4])
if (DEBUG):
	print newservernum

#step j
rcv_string = "CS 356 server sent " + str(newservernum)

print rcv_string

newservernum = newservernum + 1

reply_string = str(servernum) + " " + str(newservernum) + "\n"
if (DEBUG):
	print reply_string
newsock.send(reply_string)
newsock.close()

#step k
reply = client_sock.recv(4096)
print reply
psock.close()
client_sock.close()