from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/display', methods=['POST'])
def show_parameters():
    return render_template('display.html')


if __name__ == '__main__':
    app.run(debug=True)
