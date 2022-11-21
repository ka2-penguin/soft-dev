'''
Maya Mori
Softdev
k20 -- REST APIs
2022-11-21
time spent: 0.5
'''

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_api_key():
    key = ''
    with open('key_nasa.txt','r') as f:     # key in separate file
        key = f.read()
    # print(f'key: {key}')
    return key

def get_data():
    api_url = f"https://api.nasa.gov/planetary/apod?api_key={ get_api_key() }"
    # print(api_url)
    data = requests.get(api_url).json()
    # print(data)
    # print(type(data))
    return data         # python dictionary


# displaying the homepage
@app.route('/', methods=['GET'])
def index():
    # api_url = f"https://api.nasa.gov/planetary/apod?api_key={ get_api_key() }"
    # img_url()
    data = get_data()
    return render_template('main.html',img_url=data['url'],explanation=data['explanation'])

if __name__ == "__main__": 
    app.debug = True
    app.run()