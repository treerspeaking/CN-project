import socket
import os
import shutil

def push_to_repo(filePath:str, repoPath:str) -> bool:
    if os.path.exists(repoPath) == False: os.mkdir(repoPath)

    try:
      shutil.copy2(filePath, repoPath)
      return True
    except Exception as e:
       print("Cannot copy file at push_to_repo():", e)
       return False

def publish(fpath:str, repoPath:str, serverSocket) -> bool:
    _, fname = os.path.split(fpath)
    if push_to_repo(fpath, repoPath) == False: return False
    else: 
      serverSocket.send(f"publish {fname}".encode())
      return True