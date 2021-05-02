import os
from pydub import AudioSegment

#Diese Klasse prüft ob die gegebene Datei im MP3 Format ist und wenn ja, dann wird die Sounddatei in WAV Konvertiert, da librosa dieses Dateiformat benötigt
def convertMP3(path):
    path_to_soundfilefolder = path
    for i in os.listdir(path_to_soundfilefolder):
        end = i.split(".")[-1]
        if end == "mp3":
            src = f"{path_to_soundfilefolder}/{i}"
            sound = AudioSegment.from_mp3(src)
            i = i.split(".mp3")[0]
            dst = f"{path_to_soundfilefolder}/{i}.wav"
            sound.export(dst, format="wav")
            os.remove(src)
        else:
            print("No MP3 found")
