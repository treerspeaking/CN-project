class ServerUI:
  def __init__(self):
    pass
  
  def display_publish_file(self, fileList:dict):
    for fname, client in fileList.items():
      print(f"{fname}: {[]}")
  
  def display_available_client(self, clientList:list):
    for idx, (clientName, _) in enumerate(clientList):
      print(f"{idx}: {clientName}")