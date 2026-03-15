from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/')
def default_page():
    header_dict = request.headers
    ua = header_dict.get('User-Agent', '')
    if 'Mobile' in ua:
        return redirect('https://m.bilibili.com')
    return 'main content here...'


if __name__ == '__main__':
    app.run()
