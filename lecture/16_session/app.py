from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'CUHK'  # Seed for generating Session ID (Do not expose!)
app.config['PERMANENT_SESSION_LIFETIME'] = 1800 # Expiry: 30 minutes
app.config['SESSION_TYPE'] = 'cachelib'  # Session as files

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        if username in ['jackie', 'cuhk']:
            session['username'] = username
            return redirect(url_for('show_user'))
        else:
            error = "Invalid username. Only 'jackie' or 'cuhk' are allowed."
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/user')
def show_user():
    username = session.get('username')
    if not username:
        # If not logged on, go back to login screen
        return redirect(url_for('index'))
    return render_template('user.html', username=username)

@app.route('/logout')
def logout():
    username = session.pop('username', None)
    if username:
        print(f'Removed username: {username} from session')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
