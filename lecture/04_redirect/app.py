from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def default_page():
    url = 'https://www.cuhk.edu.hk/english/index.html'
    return redirect(url)


if __name__ == '__main__':
    app.run()
