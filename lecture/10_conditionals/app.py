from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<role>')
def welcome(role=None):
    return render_template('welcome.html', role=role)


if __name__ == '__main__':
    app.run(debug=True)
