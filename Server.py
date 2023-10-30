from ServerAPI.SendFile import *
from UI.ServerUI import ServerUI

class Server:
  def __init__(self, IP_address, port, max_client, serverUI):
    self.Server_IP = IP_address
    self.Main_port = port
    self.Capacity = max_client
    self.ServerUI = serverUI
    print("init server")
  
  def publish(self, hostname, fname):
    print("do some publish thing")
  
  def handle_server_UI(self):
    print("handle the server 's UI ")
    
  def handle_client(self, hostname):
    print("handle the client's request")
    
serverUI = ServerUI()
server = Server("192.168.1.8", 8000, 1000,serverUI)
server.ServerUI.display_publish_file()