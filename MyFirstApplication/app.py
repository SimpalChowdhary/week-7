from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return '<center><h2>Hello World!!</h2><a href="/register">Go to Register</a></center>'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        error = None
        if not username or len(username) < 3:
            error = 'Username must be at least 3 characters.'
        elif len(username) > 30:
            error = 'Username must be 30 characters or fewer.'
        elif not email:
            error = 'Email is required.'
        elif not password or len(password) < 6:
            error = 'Password must be at least 6 characters.'
        elif password != confirm_password:
            error = 'Passwords do not match.'

        if error:
            return render_template('register.html', error=error, username=username, email=email)

        return render_template('success.html', username=username)

    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html', username='Guest')

if __name__ == '__main__':
    app.run(debug=True)
