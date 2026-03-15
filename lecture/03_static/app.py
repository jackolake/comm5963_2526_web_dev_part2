from flask import Flask

app = Flask(__name__)

# Nothing is defined here
# but, people can access /static/index.html if the file is in /static folder


if __name__ == '__main__':
    app.run()
