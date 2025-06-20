from flask import Flask, request, send_from_directory, redirect, url_for, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'shared_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML = '''
<h2>Upload File</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
<h2>Files</h2>
<ul>
{% for file in files %}
  <li><a href="{{ url_for('download_file', filename=file) }}">{{ file }}</a></li>
{% endfor %}
</ul>
'''

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        return redirect(url_for('upload'))
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML, files=files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
