from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/greet')
@app.route('/greet/<name>')
def welcome(name=None):
    if name:
        return f'Hello {name}!'
    return 'Welcome'

@app.route('/boss')
def welcome_boss():
    return redirect(url_for('welcome', name='BOSS'))


if __name__ == '__main__':
    app.run()
