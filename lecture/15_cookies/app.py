from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Try to fetch currency from Cookies (Default: USD)
    currency = request.cookies.get('currency', 'USD')
    # If there is a GET request, then override
    set_currency = request.args.get('currency')
    if set_currency in ['CNY', 'HKD', 'USD']:
        currency = set_currency
    content = render_template('index.html', currency=currency)
    response = make_response(content)
    # Set the cookie for 1 hour
    response.set_cookie(key='currency', value=currency, max_age=60 * 60)
    return response


if __name__ == '__main__':
    app.run(debug=True)
