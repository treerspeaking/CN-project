def handle_fetch_request():
  send_file(Client_socket, Client_IP, lname, fname)
  
def send_file(Client_socket, Client_IP, lname, fname):
  print("send file to other client")