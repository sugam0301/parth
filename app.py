from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

api_url = "https://api.chucknorris.io/jokes/random"

@app.route('/')
def index():
    joke = get_chuck_norris_joke()
    return render_template('index.html', joke=joke)

def get_chuck_norris_joke():
    response = requests.get(api_url)
    
    joke = response.json().get('value', 'No joke available')

    return joke

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
