from ClientAPI.FetchFile import fetch, fetch_from_client, discover
from ClientAPI.PublishFile import publish
from ClientAPI.ServerHandler import return_local_file
from ClientAPI.SendFile import handle_fetch_request
from UI.ClientUI import ClientUI
import ast
import socket
import os

class Client:
  def __init__(self, server_IP_address, server_port, client_IP_address, client_port, clientUI):
    self.server_IP = server_IP_address
    self.server_port = server_port
    self.User_IP = client_IP_address
    self.Port_num = client_port
    self.ClientUI = clientUI
    self.ClientName = input("Input client name: ")

    self.repoPath = "repository"
    # if os.path.exists(self.repoPath): 
    #   self.published_file = os.listdir(self.repoPath)
    #   discover(self.server_socket, self.published_file)
    # else: self.published_file = []

    self.published_file = []

    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.connect((self.server_IP, self.server_port))
    print("init client")
  
  def handle_client(self):
    print("handle other client's request")
    
  def handle_server(self, server_socket):
    # Extract server address
    server_address = server_socket.getpeername()
    fetch(server_socket)

    # Handle the messages from the server
    while True: 
        msg = server_socket.recv(1024).decode('utf-8')
        if len(msg) == 0:
              print("Connection closed by the server.")
              break
        print(f"Received message from {server_address}: {msg}")

        # Check the type of message from client. 
        msg = msg.split(None, 1)
        if msg[0] == "discover":
          discover(server_socket, self.published_file)     

  def handle_client_UI(self, server_socket):
     command = input().split(' ')
     if command[0] == "fetch":
        fetch(server_socket)
     elif command[0] == "publish":
        if publish(command[1], "repository", server_socket):
          self.published_file.append(command[1])
          self.ClientUI.display_published_file(self.published_file)
        else:
          print("Cannot publish file to server")
     else:
        print(f"Undefined command: {command[0]}")
  
  def request_server_file(self):
    handle_fetch_request()

if __name__ == "__main__": 
  clientUI = ClientUI()
  client1 = Client("127.0.0.1", 12345, "192.168.1.8", 8000, clientUI)
  client1.handle_server()
  client1.ClientUI.display_available_file()