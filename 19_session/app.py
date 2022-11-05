'''
Metamorphosis: Eric Sohel, Yuki Feng, Maya Mori, Aleksandra Shifrina
Softdev
k12 -- GET vs. POST, displaying form responses
2022-10-17
time spent: 1.2
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

@app.route('/', methods=['GET'])
def index():
    print(session)
    # print(request.cookies)
    print(request.cookies.get('username'))
    # if request.cookies.get('username') is not None:
    if 'username' in session:
        return render_template('response.html',username=session["username"])
    return render_template('login.html',has_error=False)
    # session.pop('username', None)
    # if 'username' in session:
    #     return render_template('response.html',username=session["username"])
    # return render_template('login.html',good_password=password)

@app.route('/', methods=['POST'])
def login():
    print('login function')
    if request.form['username'] == username and request.form['password'] == password:
        session['username'] = request.form['username']
        return render_template('response.html',username=session["username"])
    # if request.method == 'POST':

    error_type = ''
    if request.form['username'] != username:
        error_type='username'
    elif request.form['password'] != password:
        error_type = 'password'

    return render_template('login.html',has_error=True,error=error_type)
    # session['username'] = request.form['username']

@app.route('/logout',methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('login.html')


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()