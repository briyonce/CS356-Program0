import socket 	# Used to create client_socket
import random 	# Used to generate usernum
import sys 		# Used to exit the program upon failure

DEBUG = 0		# Debug flag


#Part i
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create new client socket
initval = client_socket.getsockname() # This should be ('0.0.0.0', 0)

#Part ii
client_socket.connect(('128.83.144.56',35603)) # Connect to server at port 35603

tok = client_socket.getsockname() # This will return updated client socket info: (addr,port)
if(tok == initval): # Socket info will remain unchanged if the connection fails
	sys.exit("Server connection failed.")

#Part iii
usernum  = random.randint(1,9001) # Generate random usernum

req_string = "ex0 128.83.144.56-35603 " + str(tok[0]) + "-" + str(tok[1]) + " " + str(usernum) + " B.M.Bradshaw\n"

#Part iv
client_socket.send(req_string)

#Part v
reply1 = client_socket.recv(4096) # Something along these lines: CS 356 Server Tue Oct 03 18:44:26 CDT 2017
reply2 = client_socket.recv(4096) # Something along these lines: OK 6174 B.M.Bradshaw 9109160
str2tokens = reply2.split(" ")
if(DEBUG):
	print reply1
	print reply2

if (len(str2tokens) < 4): # str2tokens should be something like: ['OK', '6174', 'B.M.Bradshaw', '9109160\n']
	sys.exit("SERVER REPLY ERROR")
if (str2tokens[0] != "OK"): # The server did not send back OK
	sys.exit("ACK ERROR")
if (int(str2tokens[1]) != (usernum + 1)): # The server did not increment the usernum
	sys.exit("USERNUM ERROR, " + str(usernum) + ", " + str(str2tokens[1]))

newUN = int(str2tokens[1]) # The incremented usernum
servernum = int(str2tokens[3])
print servernum # Instructions said to output servernum

#Part vi
servernum = servernum + 1
ack_string = "ex0 " + str(newUN) + " " + str(servernum) + "\n"
client_socket.send(ack_string)

#Part vii
reply = client_socket.recv(4096) # Something like: CS 356 Server Tue Oct 03 18:44:26 CDT 2017 OK 9109161\n
if(DEBUG):
	print reply

replytoks = reply.split(" ")
OKFND = 0 # Flag that is activated whenever we find "OK" in the reply
index = 0
while (index < len(replytoks) and (not OKFND)):
	if(replytoks[index] == "OK"):
		OKFND = 1
	else:
		index = index + 1

#Part viii
if ((reply[len(reply) - 1] == "\n") and OKFND): # \n should be at the end of the reply
	#print("Closing socket...")
	client_socket.close()

