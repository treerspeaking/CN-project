class ClientUI:
  def __init__(self):
    pass
  
  def display_published_file(self, listFile):
    print("List of published files:")
    for idx, fname in enumerate(listFile):
      print(f"{idx}: {fname}")
    
  def make_fetch_request(self):
    print("make a fetch request for some file")
    
  def make_publish_request(self):
    print("make a publish request of file x to server y")
    
def display_available_file(list_of_file):
     list_of_file = list_of_file.split()
     print(f"There are {len(list_of_file)} files: ")

     for idx, file in enumerate(list_of_file):
          print(f"{idx+1}. {file}")
     chosen_idx = int(input(f"Please choose a file by typing the index: "))
     return list_of_file[chosen_idx-1]