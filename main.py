from flask import Flask, render_template, request, flash, send_from_directory
from werkzeug.utils import secure_filename
import os, json, threading, time
from functions import *
import shortuuid
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "dslaifjk"

value = [
        ["cpng","PNG"],
        ["cjpg","JPG"],
        ["cjpeg","JPEG"],
        ["cwebp","WEBP"],
        ["ctif","TIF"],
        ["cbmp","BMP"],
        ["ctiff","TIFF"],
        ["cgray","Grayscale"]
    ]

def cleanGarbage():
    threading.Timer(600, cleanGarbage).start()
    for file in os.listdir(UPLOAD_FOLDER):
        if file != ".gitkeep":
            os.remove(os.path.join(UPLOAD_FOLDER,file))
    print(f'Garbage Cleaned at {time.strftime("%m/%d/%Y, %H:%M:%S")}.')

cleanGarbage()

def normalToast(message,category):
    return   f'''<div class="toast show align-items-center text-bg-{category} border-0" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body">
                    {message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                </div>'''         
 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def home():
    return render_template("index.html",values=value)

@app.route('/api/convert', methods=['GET','POST'])
def api():
    if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                return normalToast("No File Part.","danger")
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                return normalToast("No Selected File.","danger")
            if request.form["operation"] == "":
                return normalToast("Please Select an File Format","danger")
             
            if not allowed_file(file.filename):
                                return normalToast(f"Please enter an Image.","danger")
                
                
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = ".".join(filename.split(".")[:-1]) + "_" + shortuuid.uuid() + "." + filename.split(".")[-1]
                originalFilename = filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filename = processImage(filename,request.form['operation'])
                
                if filename != originalFilename: 
                    os.remove(os.path.join(UPLOAD_FOLDER,originalFilename))

                return normalToast(f"Your Image is processed Sucessfully. Click <a class='alert-link' href='/static/uploads/{filename}' download>here</a> to Download.","success")


@app.route('/privacy-policy')
def privacyPolicy():
    return render_template("privacy-policy.html")

@app.route('/about-us')
def aboutUs():
    return render_template("about-us.html")

@app.route('/contact-us')
def contactUs():
    return render_template("contact-us.html")

app.run(debug=True)