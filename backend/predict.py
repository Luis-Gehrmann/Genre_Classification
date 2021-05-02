import pickle
import os
import soundfile as sf
import math
from pydub import AudioSegment
from pathlib import Path 
import numpy as np
import librosa
import librosa.display

#Klasse um aus einer Song Datei eine Aussage über das vorliegende Genre zu treffen 
def predictSound(path):
  path_to_soundfilefolder = path+"/Input"
  
  #Länge eines Samples ist 3 Sekunden
  soundLength = 3

  filenumber = 0

  
  #Schneide den Inputsong in 3 Sekundenstücke, welche als Input Menge für das preprocessing dienen 
  for i in os.listdir(path_to_soundfilefolder):
      filenumber +=1
      file = os.path.join(path_to_soundfilefolder, i)
      f = sf.SoundFile(file)
      seconds = (len(f) / f.samplerate)
      slicecount=math.floor(seconds/soundLength)
      for slicenumber in range(slicecount):
          t1=slicenumber*soundLength*1000 #da Millisekunden
          t2=t1 + soundLength*1000 #hat die Länge in Sekunden von soundLength
          newAudio = AudioSegment.from_wav(file)
          newAudio = newAudio[t1:t2]
          filename = i.split(".wav")[0]
          newAudio.export(f"{path}/processed_Input/{filename}_{slicenumber}.wav", format="wav")
      print("Audio Sliced")    
  #Update der Variable auf den Pfad für zerschnittetene Songfragmente
  path_to_soundfilefolder = path+"/processed_Input/"

  #enthält sämtliche Eigenschaften der Einträge
  features = []

  #enthält sämtliche Namen der Einträge
  filenames = []
  
  print("Attribute Folder: "+path_to_soundfilefolder)

  for filename in os.listdir(path_to_soundfilefolder):
      #Name der Datei wird abgespeichert, um ihn am Ende auszugeben
      filenames.append(filename)

      #hier kommen alle Attribute pro Soundfile rein
      attributes = []

      #Umwandlung der Soundfiles in repräsentative Zahlenwerte
      print(f"Converting: {filename}")
      y, sr = librosa.load(path_to_soundfilefolder + filename)

      #extrahieren der aussagekräftigen Song Eigenschaften mithilfe der Librosa Libary
      stft_array = librosa.feature.chroma_stft(y=y, sr=sr)
      stft_mean = np.mean(stft_array)
      stft_var = np.var(stft_array)

      cq_array = librosa.feature.chroma_cqt(y=y, sr=sr)
      cq_mean = np.mean(cq_array)
      cq_var = np.var(cq_array)

      rms_array = librosa.feature.rms(y=y)
      rms_mean = np.mean(rms_array)
      rms_var = np.var(rms_array)

      cent_array = librosa.feature.spectral_centroid(y=y, sr=sr)
      cent_mean = np.mean(cent_array)
      cent_var = np.var(cent_array)

      spec_array = librosa.feature.spectral_bandwidth(y=y, sr=sr)
      spec_mean = np.mean(spec_array)
      spec_var = np.var(spec_array)

      rolloff_array = librosa.feature.spectral_rolloff(y=y, sr=sr)
      rolloff_mean = np.mean(rolloff_array)
      rolloff_var = np.var(rolloff_array)

      zero_crossing_rate_array = librosa.feature.zero_crossing_rate(y)
      zero_crossing_rate_mean = np.mean(zero_crossing_rate_array)
      zero_crossing_rate_var = np.var(zero_crossing_rate_array)

      tonnetz_array = librosa.feature.tonnetz(y=y, sr=sr)
      tonnetz_mean = np.mean(tonnetz_array)
      tonnetz_var = np.var(tonnetz_array)

      y_harmonic_array, y_percussive = librosa.effects.hpss(y)
      tempo1, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
      tempo = np.float32(tempo1)

      y_harmonic_mean = np.mean(y_harmonic_array)
      y_harmonic_var = np.var(y_harmonic_array)

      attributes.extend([stft_mean, stft_var, cq_mean, cq_var, rms_mean, rms_var, cent_mean, cent_var, spec_mean, spec_var, rolloff_mean, rolloff_var, zero_crossing_rate_mean, zero_crossing_rate_var, tonnetz_mean, tonnetz_var, tempo, y_harmonic_mean, y_harmonic_var]) 

      #das mfcc-array besteht aus 20 arrays, für die jeweils mean und var bestimmt werden
      mfcc_array = librosa.feature.mfcc(y=y, sr=sr)
      for i in range(20):
          mfcc_mean = np.mean(mfcc_array[i])
          mfcc_var = np.var(mfcc_array[i])
          attributes.extend([mfcc_mean, mfcc_var])  


      #Anhängen eines Eintrages
      features.append(attributes)
  
  import pandas as pd
  import sklearn.preprocessing as skp
  import joblib

  # Normalisieren der Daten mithilfe des vorgegebenen Scalers
  df = pd.DataFrame(features) 
  cols = df.columns
  min_max_scaler = joblib.load(f'Programm/scaler.gz')
  np_scaled = min_max_scaler.transform(features)
  features_normalized = pd.DataFrame(np_scaled, columns = cols)

  print(features_normalized)
  
  #Model laden
  from tensorflow import keras
  loaded_model = keras.models.load_model(f'Programm/model_saved')
  #Dict laden
  #Pickle load:
  with open(f'Programm/prediction_index.p', 'rb') as fp:
      prediction_index = pickle.load(fp)
  
    #Model anwenden
  loaded_model.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

  predictions = loaded_model.predict(features_normalized)
  prediction = np.argmax(predictions,1)

      
  genreCountList = [0] * len(prediction_index)
  genreCount = np.asarray(genreCountList)

  for i in range(len(prediction)):
      print(f"Soundfile {filenames[i]}: Ausgabe: {prediction_index[prediction[i]]} mit Confidence: {predictions[i][prediction[i]]}")

      #Wie häufig wurde jedes Genre genannt
      genreCount[prediction[i]]+=1

  for i in range(len(genreCount)):
          for j in range(len(genreCount) - (i+1)):
              if genreCount[j] < genreCount[j+1]:
                  # Swap
                  genreCount[j], genreCount[j+1] = genreCount[j+1], genreCount[j]
                  prediction_index[j], prediction_index[j+1] = prediction_index[j+1], prediction_index[j]

  count = 0
  for i in prediction_index:
      print(f"Platz {count} ist {prediction_index[i]} mit einer Häufigkeit von {genreCount[i]}")
      count+=1
  
  return prediction_index
