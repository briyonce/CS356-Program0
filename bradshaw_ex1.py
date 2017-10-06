import socket
import random
import sys

DEBUG = 0

psock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create new server socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if (DEBUG):
	print client_sock.getsockname()
client_sock.connect(('128.83.144.56', 35603))
addr = client_sock.getsockname()
if (DEBUG):
	print addr
psock.bind((addr[0],0))
addr = psock.getsockname()
print ("Address: " + str(addr[0]) + " Port: " + str(addr[1]))
port = addr[1]
psock.listen(5)
usernum = random.randint(1,9001)
req_string = "ex1 128.83.144.56-35603 " + str(addr[0]) + "-" + str(addr[1]) + " " + str(usernum) + " B.M.Bradshaw\n"
if(DEBUG):
	print req_string
client_sock.send(req_string)
reply1 = client_sock.recv(4096)
reply2 = client_sock.recv(4096)
if(DEBUG):
	print reply2
reply2tok = reply2.split(" ")
if(DEBUG):
	print reply2tok

if(reply2tok[0] != "OK"):
	sys.exit("ACK ERROR")

servernum = int(reply2tok[3]) + 1

temp = (psock.accept())
newsock = temp[0]
if (DEBUG):
	print newsock
	print newsock.getsockname()
reply = newsock.recv(4096)
if (DEBUG):
	print reply
replytok = reply.split(" ")
newservernum = int(replytok[4])
if (DEBUG):
	print newservernum

rcv_string = "CS 356 server sent " + str(newservernum)

print rcv_string

newservernum = newservernum + 1

reply_string = str(servernum) + " " + str(newservernum) + "\n"
if (DEBUG):
	print reply_string
newsock.send(reply_string)

reply = client_sock.recv(4096)

print reply

newsock.close()
psock.close()
client_sock.close()

