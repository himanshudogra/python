from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
    return '...Jai Baba Swami to All...'

if __name__ == '__main__':
 app.run(debug=True)