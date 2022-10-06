'''
<Frist> <Lsat>
SoftDev
K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
<yyyy>-<mm>-<dd>
time spent: <elapsed time in hours, rounded to nearest tenth>
'''

from flask import Flask

# why are there underscores before and after 'name'?
app = Flask(__name__) # assigns new instance of Flask to app
#print(__name__)

@app.route("/") # root route request, slash is needed

# function runs regardless of its name
def hello_world():
    print('hello')#__name__) # why does this print '__main__'?
    return 'hi'#"No hablo queso!"  # what is written in web browser

app.run()  # Flask app runs

'''
- whatever is returned in hello_world is displayed on web browser
- whatever is printed in the function prints in the terminal
- the string in @app.route() needs to follow the localhost url
'''
                
