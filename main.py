from flask import Flask, render_template, request, flash, redirect , url_for
from werkzeug.utils import secure_filename
import os, cv2
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "dslaifjk"

def processImage(filename,operation):
    img = cv2.imread(f"uploads/{filename}")
    
    match operation:
        case "cgray":
            imgProcessed = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"static/{filename}", imgProcessed)
            return(filename)
        case "cwebp":
            imgProcessed = cv2.imwrite(f"static/{filename.split('.')[0]}.webp", img)
            return(f"{filename.split('.')[0]}.webp")
        case "cpng":
                imgProcessed = cv2.imwrite(f"static/{filename.split('.')[0]}.png", img)
                return(f"{filename.split('.')[0]}.png")
        case "cjpg":
                imgProcessed = cv2.imwrite(f"static/{filename.split('.')[0]}.jpg", img)
                return(f"{filename.split('.')[0]}.jpg")
        
    print(f"The filename is {filename} & operation is {operation}")
    

@app.route('/')
def home():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "Error no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename = processImage(filename,request.form['operation'])
            flash(f"your image has been processed and is saved <a href='/static/{filename}'>here</a>")
    return render_template("index.html")

app.run(debug=True)