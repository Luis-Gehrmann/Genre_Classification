import os
from pydub import AudioSegment



    os_dir = os.getcwd()
    path_to_soundfilefolder = f"{os_dir}\\test"
    for i in os.listdir(path_to_soundfilefolder):
        if ".mp3" in i:
            src = f"{path_to_soundfilefolder}\\{i}"
            sound = AudioSegment.from_mp3()
            i = i.split(".mp3")[0]
            dst = f"{path_to_soundfilefolder}\\{i}.wav"
            sound.export(dst, format="wav")