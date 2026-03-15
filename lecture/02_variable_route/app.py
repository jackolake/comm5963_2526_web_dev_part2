from flask import Flask

app = Flask(__name__)


@app.route('/user/profile')
@app.route('/user/profile/<user>')
def profile(user=None):
    if user:
        return f'Welcome to {user}'
    return 'Specify a profile'


if __name__ == '__main__':
    app.run()
