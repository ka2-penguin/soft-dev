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

app = Flask(__name__)

@app.route("/")
def disp_loginpage():
    request.cookies.get()