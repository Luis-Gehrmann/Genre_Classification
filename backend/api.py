import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from createUser import init
from predict import predictSound

ALLOWED_EXTENSIONS = {'csv','mp3','wav'}
app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/getFile', methods=['Get','POST'])
def getFile():
    UPLOAD_FOLDER = init()
    if request.method == 'POST':
      f = request.files['file']
      f.save(UPLOAD_FOLDER+"/Input/"+secure_filename(f.filename))
      predictSound(UPLOAD_FOLDER)
      return 'file uploaded successfully'
    
