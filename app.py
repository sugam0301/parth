from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

api_url = "https://api.chucknorris.io/jokes/random"

@app.route('/')
def index():
    response = requests.get(api_url)
    
    joke = response.json().get('value', 'No joke available')
    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
