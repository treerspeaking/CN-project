from ServerAPI.SendFile import *
from UI.ServerUI import ServerUI
import socket

class Server:
  def __init__(self, IP_address, port, max_client, serverUI):
    self.Server_IP = IP_address
    self.Main_port = port
    self.Capacity = max_client
    self.ServerUI = serverUI
    self.available_file_list = {}
    self.index_list = {}  # key: FileName and value: [ClientSocket]

    self.client_list = {} # key: ClientName and value: IP and Port

    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # server_socket.bind((self.Server_IP, self.Main_port))
    # server_socket.listen(self.Capacity)
    print("init server")
  
  def publish(self, hostname, fname):
    if fname in self.available_file_list.keys():
        self.available_file_list[fname].append(hostname)
    else:
        self.available_file_list[fname] = [hostname]
    update_file_list(hostname, fname)

  def update_available_file(list_file):
    print("Have not yet implement Update_availabel_file function in Server")
  
  def handle_server_UI(self):
    while True:
      command = input().split(" ")
      if command[0] == "Display":
        ServerUI.display_publish_file(self.available_file_list)

      elif command[0] == "Discover":
        serverUI.display_available_client(self.client_list)
        clientName = input("Client name: ")
        file_list = discover(self.client_list[clientName])
        self.update_available_file(file_list)

      elif command[0] == "Ping":
        serverUI.display_available_client(self.client_list)
        clientName = input("Client name: ")
        ping(self.client_list[clientName])

      else: print("Undefined command")
    
  def handle_client(self, client_socket):
      # Extract client address
      client_address = client_socket.getpeername()
      print(client_address)

      # handle the messages from the client
      while True: 
            msg = client_socket.recv(1024).decode('utf-8')
            if len(msg) == 0:
                print("Connection closed by the client.")
                return
            print(f"Received message from {client_address}: {msg}")

            # Check the type of message from client 
            msg = msg.split(None, 1)
            if msg[0] == "publish":
                self.publish(client_socket, msg[1])
            elif msg[0] == "fetch":
                handle_fetch(client_socket)
    

if __name__ == "__main__":
  serverUI = ServerUI()
  server = Server("192.168.1.8", 8000, 1000, serverUI)
  server.ServerUI.display_publish_file()