import os
from pydub import AudioSegment

def convertMP3(path):
    path_to_soundfilefolder = path
    for i in os.listdir(path_to_soundfilefolder):
        end = i.split(".")[-1]
        if end == "mp3":
            src = f"{path_to_soundfilefolder}\\{i}"
            sound = AudioSegment.from_mp3()
            i = i.split(".mp3")[0]
            dst = f"{path_to_soundfilefolder}\\{i}.wav"
            sound.export(dst, format="wav")
        else:
            print("No MP3 found")
