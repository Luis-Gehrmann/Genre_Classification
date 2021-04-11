import os
from pathlib import Path 
import pickle
import uuid

def init():
    client_id = uuid.uuid4()
    os_dir = os.getcwd()
    #Create Folders if programm folder not exists
    Path(f"{os_dir}\\Clients\\").mkdir(parents=True, exist_ok=True)
    Path(f"{os_dir}\\Clients\\"+str(client_id)).mkdir(parents=True, exist_ok=True)
    Path(f"{os_dir}\\Clients\\"+str(client_id)+"\\Input").mkdir(parents=True, exist_ok=True)
    Path(f"{os_dir}\\Clients\\"+str(client_id)+"\\processed_Input").mkdir(parents=True, exist_ok=True)

    path_to_soundfilefolder = f"{os_dir}\\Clients\\"+str(client_id)+"\\Input"
    return path_to_soundfilefolder
