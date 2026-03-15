from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def show_parameters():
    return render_template('display.html', args=request.args)


if __name__ == '__main__':
    app.run(debug=True)
