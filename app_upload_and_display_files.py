from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if not os.path.exists(app.config['UPLOAD_FOLDER']) :
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_files(filename) :
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def upload_file() :
    if request.method == 'POST' :    
        if 'file' not in request.files :
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '' :
            return redirect(request.url)
        if file and allowed_files(file.filename) :
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)
    
@app.route('/uploads/<filename>')
def uploaded_file(filename) :
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__' :
    app.run(port=5010, debug=True)
