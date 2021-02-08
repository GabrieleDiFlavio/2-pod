from flask import Flask, jsonify, request
from random import random
import urllib




# insert flask annotation here
app = Flask(__name__)


@app.route('/')
def _sum():
    # A: first number to sum
    # B: second number to sum
    sum = request.args.get('somma', default=0, type=float)
    #b = request.args.get('b', default=0, type=float)
    prodotto = sum*5
    
    #URL = "sum-s"
    #r = requests.get(url = URL, PARAMS = sum)
    return jsonify({'result': prodotto})

#contents = urllib.request.urlopen(URL:5000?somma=sum) 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
