import os
import shutil
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from createUser import init
from predict import predictSound
from convert import convertMP3

#Erlaubte Dateien Definieren
ALLOWED_EXTENSIONS = {'csv','mp3','wav'}
app = Flask(__name__)

#Check, ob die Datei das richtige Format hat
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Definition der Route / API ereichbar unter localhost:5000/getFile
@app.route('/getFile', methods=['Get','POST'])
def getFile():
    #Aufruf der Funktion init der Klasse CreateUser
    UPLOAD_FOLDER = init()
    if request.method == 'POST':
      #Speichern der Soundatei, welche im POST Befehl mitgeliefert wurde  
      f = request.files['file']
      f.save(UPLOAD_FOLDER+"/Input/"+secure_filename(f.filename))
      #Konvertierung von MP3 zu WAV falls nötig
      convertMP3(UPLOAD_FOLDER+"/Input/")
      #Soundprediction durch das neuronale Netzwerk
      predictionsList = predictSound(UPLOAD_FOLDER)
      #Löschen des angelegten Nutzerordners und Rückgabe der Predictions
      shutil.rmtree(UPLOAD_FOLDER)
      return str(predictionsList[0]+","+predictionsList[1]+","+predictionsList[2])
    
