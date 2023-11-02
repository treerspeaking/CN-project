import socket

def choose_client(filename, available_file_list, index_list):
     avail_client = available_file_list[filename]
     chosen_index = index_list[filename]
     chosen_client = avail_client[chosen_index]

     # Update the index dict
     index_list[filename] = (chosen_index + 1) % len(avail_client)
     return chosen_client

def handle_fetch(client_socket, available_file_list, index_list):
     # Extract client address
     client_address = client_socket.getpeername()

     # Send list of available file to client 
     list_of_file = available_file_list.keys()
     msg = "list " + ' '.join(map(str, list_of_file))
     client_socket.sendall(msg.encode('utf-8'))
     print(f"Send list of available files to {client_address}")

     # Receive the chosen file and send the suitable client
     filename = client_socket.recv(1024).decode('utf-8')
     print(filename)
     if len(filename) == 0:
          print("Connection closed by the client.")
          return 
     chosen_client = choose_client(filename, available_file_list, index_list)
     msg = "client " + chosen_client
     client_socket.sendall(msg.encode('utf-8'))
     print(f"Send information of client {chosen_client} for {filename} to {client_address}")
  
def update_file_list(hostname, fname):
   print("Do not need to use Update_file_list function in SendFile.py")

# Vấn đề chưa biết code như nào ???
def ping(clientIP, clientPort):
   print("Have not yet implement ping in Server function")

# def discover(client_socket):
#   msg = "discover"
#   client_socket.sendall(msg.encode('utf-8'))

#   msg = client_socket.recv(1024).decode('utf-8')
#   if len(msg) == 0:
#       print("Connection closed by the client.")
#       return
#   msg = msg.split()
#   return msg 

def discover(clientIP, clientPort):
  connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  connection.connect((clientIP, clientPort))

  connection.sendall("discover".encode())
  strFileList = connection.recv(1024).decode()

  return strFileList.split(" ")
   

def check_file():
  print("check if the requested file exist")
  
def send_host_IP(hostname):
  print("send the IP of the client that has the requested file to hostname")