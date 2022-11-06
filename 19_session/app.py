'''
Metamorphosis: Eric Sohel, Yuki Feng, Maya Mori, Aleksandra Shifrina
Softdev
k19 -- sessions in Flask
2022-11-04
time spent: 2.0
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template 
from flask import request
from flask import session

import os

app = Flask(__name__)

app.secret_key = os.urandom(32)
username = 'bob'
password = 'mob123'

# displaying the homepage
@app.route('/', methods=['GET'])
def index():
    print(session)
    # print(request.cookies)
    print(request.cookies.get('username'))
    if 'username' in session:
        return render_template('response.html',username=session["username"])
    return render_template('login.html',has_error=False)

# if user tried to login in
@app.route('/', methods=['POST'])
def login():
    print('login function')

    # if everything matches
    if request.form['username'] == username and request.form['password'] == password:
        # add session
        session['username'] = request.form['username']
        return render_template('response.html',username=session["username"])

    # handle cases when username/password in wrong
    error_type = ''     # error message
    if request.form['username'] != username:
        error_type='Username not found'
    elif request.form['password'] != password:
        error_type = 'Wrong password'
    return render_template('login.html',has_error=True,error=error_type)
    # session['username'] = request.form['username']

@app.route('/logout',methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('login.html')


if __name__ == "__main__": 
    app.debug = True
    app.run()