from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome!'

@app.errorhandler(404)
def handle_not_found(error):
    msg = f'[{error.code}] {request.path} not found'
    return msg, error.code

if __name__ == '__main__':
    app.run()
