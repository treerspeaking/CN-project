def display_published_file():
  print("published file :")
  
def make_fetch_request():
  print("make a fetch request for some file")
  
def make_publish_request():
  print("make a publish request of file x to server y")
  
def display_available_file(list_of_file):
     list_of_file = list_of_file.split()
     print(f"There are {len(list_of_file)} files: ")

     for idx, file in enumerate(list_of_file):
          print(f"{idx+1}. {file}")
     chosen_idx = int(input(f"Please choose a file by typing the index: "))
     return list_of_file[chosen_idx-1]