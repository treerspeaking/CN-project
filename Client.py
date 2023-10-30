from ClientAPI.FetchFile import fetch
from ClientAPI.PublishFile import publish
from ClientAPI.ServerHandler import return_local_file
from ClientAPI.SendFile import handle_fetch_request
from UI.ClientUI import ClientUI

class Client:
  def __init__(self, IP_address, port, clientUI):
    self.User_IP = IP_address
    self.Port_num = port
    self.ClientUI = clientUI
    print("init client")
  
  def handle_client(self):
    print("handle other client's request")
    
  def handle_server(self):
    return_local_file("servername")
    
  def handle_client_UI(self):
    publish("some file")
  
  def request_server_file(self):
    handle_fetch_request()

clientUI = ClientUI()
client1 = Client("192.168.1.8", 8000, clientUI)
client1.handle_server()
client1.ClientUI.display_available_file()