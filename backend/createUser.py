import os
from pathlib import Path 
import pickle
import uuid

#Diese Klasse erstellt für jeden Upload einen nutzerspezifischen Ordner in den die Sound Datei und verarbeitete Sounddateien gespeichert werden
def init():
    client_id = uuid.uuid4()
    #Create Folders if programm folder not exists
    Path("Clients").mkdir(parents=True, exist_ok=True)
    Path("Clients/"+str(client_id)).mkdir(parents=True, exist_ok=True)
    Path("Clients/"+str(client_id)+"/Input").mkdir(parents=True, exist_ok=True)
    Path("Clients/"+str(client_id)+"/processed_Input").mkdir(parents=True, exist_ok=True)

    path_to_soundfilefolder = "Clients/"+str(client_id)
    return path_to_soundfilefolder
