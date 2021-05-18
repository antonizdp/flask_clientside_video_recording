import os

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './files/'
os.makedirs('./files/', exist_ok=True)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'videoFile' not in request.files:
            print('No file part')
        else:
            file = request.files['videoFile']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                print('No selected file')
            elif file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect('/')


app.run(debug=True)
