from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/process', methods=['POST'])
def process_result():
    img = request.files.get('image')
    filename = None
    if img:
        filename = img.filename
        path = f"{app.root_path}/{app.config['UPLOAD_FOLDER']}/{filename}"
        img.save(path)
    return render_template('display.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
