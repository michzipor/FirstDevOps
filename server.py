# importing the socket library 
import socket
# importing the requests from urllib  
import requests 
  
def main():
	LISTEN_PORT = 80

	# Create a TCP/IP socket
	listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Binding to local port 80
	server_address = ('', LISTEN_PORT)
	listening_sock.bind(server_address)

	# Listen for incoming connections
	listening_sock.listen(1)

	# Create a new conversation socket
	client_soc, client_address = listening_sock.accept()

	# Receiving data from the client
	client_msg = client_soc.recv(1024)
	client_msg = client_msg.decode()
	# get first argument (name) from url string
	client_msg = client_msg.split("?")[1]
	# get name value from first url argument
	my_name = client_msg.split("=")[1]
	
	# Sending data back
	msg = "Hello, " + my_name + "!"
	client_soc.sendall(msg.encode())

	# Closing the conversation socket
	client_soc.close()

	# Closing the listening socket
	listening_sock.close()

if __name__ == "__main__":
    main()
