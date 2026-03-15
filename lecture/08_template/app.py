from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    content = 'Welcome Home!'
    return render_template('layout.html', content=content)


@app.route('/about')
def about():
    content = 'About Us'
    return render_template('layout.html', content=content)


if __name__ == '__main__':
    app.run(debug=True)
