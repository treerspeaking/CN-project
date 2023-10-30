def fetch(fname):
  fetch_from_client(Client_socket, Client_IP, lname, fname)

def fetch_from_client(Client_socket, Client_IP, lname, fname):
  print("send fetch request to other client")