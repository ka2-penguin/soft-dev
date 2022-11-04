'''
Metamorphosis: Eric Sohel, Yuki Feng, Maya Mori, Aleksandra Shifrina
Softdev
k12 -- GET vs. POST, displaying form responses
2022-10-17
time spent: 0.8
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template 
from flask import request

from flask import session

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'foo'
username = 'bob'
password = 'mob123'




@app.route('/')
def index():
    print(session)
     session.pop('username', None)
    if 'username' in session:
        return render_template('response.html',username=session["username"])
    return render_template('login.html',good_password=password)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        if request.form['username'] == username and request.form['password'] == password:
            return render_template('response.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()