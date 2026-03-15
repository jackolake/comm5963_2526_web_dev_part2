from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_schools():
    schools = {
        'CUHK': 'https://www.cuhk.edu.hk',
        'HKU': 'https://www.hku.hk',
        'HKUST': 'https://hkust.edu.hk'
    }
    return render_template('school.html', schools=schools)


if __name__ == '__main__':
    app.run(debug=True)
