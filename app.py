
from flask import Flask,jsonify,request
from flask_cors import CORS
from helpers.dbhelpers import run_query
import sys 

app = Flask(__name__)
CORS(app)
@app.get('/api/animals')
def animal_get():
    # DB select
    animal_list = []
    return jsonify(animal_list), 200
    
    
    
    

@app.post('/api/animals/')
def animal_post():
    data = request.json
    animal_name = data.get('animalName')
    image_url = data.get('imageUrl')
    #if animal name is equal to none
    if not animal_name:
        return jsonify("missing required argument 'animalName'"),422
    if not image_url :
        return jsonify("missing required argument : 'imageUrl'"),422
    #error checking the actual values for the arguments
    # DB write


