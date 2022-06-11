
from flask import Flask,jsonify,request

from helpers.dbhelpers import run_query
import sys 

app = Flask(__name__)

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
    return jsonify("animal added"), 200

if len(sys.argv) > 1:
    mode = sys.argv[1]
    print (sys.argv[0])
    print (sys.argv[1])
else:
    print("missing requriement argument: testing")
    exit()

if mode == "testing":
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif mode == "production":
    import bjoern
    print("running production mode")
    bjoern.run(app, "0.0.0.0", 5005)
else:
    print("invalid mode, please chose either 'testing' or 'production'")
    exit()