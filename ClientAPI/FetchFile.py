from ClientUI import display_available_file
import ast
import socket

def fetch(server_socket):
     # Extract server address
     server_address = server_socket.getpeername()

     msg = "fetch"
     server_socket.sendall(msg.encode('utf-8'))
     print(f"Send fetch requests to server")

     for _ in range(2):
          msg = server_socket.recv(1024).decode('utf-8')
          if len(msg) == 0:
               print("Connection closed by the server.")
               break
          print(f"Received message from {server_address}: {msg}")

          # Check the type of message from client. 
          msg = msg.split(None, 1)
          if msg[0] == "list": # return a list of available file from fetch request. User will choose a file, then client will send the request for info of that file
               chosen_file = display_available_file(msg[1])
               server_socket.sendall(f"{chosen_file}".encode('utf-8'))
          elif msg[0] == "client": # return the info of a client having the chosen file
               fetch_from_client(chosen_file, msg[1])


def fetch_from_client(chosen_file, target_address):
     print(target_address)
     target_address = ast.literal_eval(target_address) # Convert to a tuple
     fetch_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     fetch_socket.connect(target_address)

     msg = f"fetch {chosen_file}"
     fetch_socket.sendall(msg.encode('utf-8'))
     with open(f'{chosen_file}.txt', 'wb') as file:
          data = fetch_socket.recv(4096)  # Adjust buffer size as per your requirements
          file.write(data)

def discover(server_socket, published_file):
     msg = ' '.join(map(str, published_file))
     server_socket.sendall(msg.encode('utf-8'))
     print(f"Send published filenames to server")