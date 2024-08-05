from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for demonstration purposes
users = []

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simple validation
        if username and password:
            users.append({'username': username, 'password': password})
            return redirect(url_for('success'))
        else:
            return 'Please provide both username and password.'

    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)