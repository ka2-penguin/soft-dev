# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route

# runs everytime you reload the site
def hello_world():
    return "No hablo queso!"

app.run()

'''
- '__main__' won't be printed in terminal
- same as v0 otherwise
'''
