
from flask import Flask,jsonify,request
from flask_cors import CORS
import sys 

app = Flask(__name__)
CORS(app)

@app.get('/api/animalName')
def animal_get():
    params = request.args
    print(params)
