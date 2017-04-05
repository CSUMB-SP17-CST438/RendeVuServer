import os
import sys
import json
import requests
import time
from flask import Flask, render_template, request, jsonify, abort, make_response

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1.0/postInfo', methods=['POST'])
def create_task():
    log("someone pinged the api")
    log(request.json)
    
    #if the json data does not have the 'usedID' header
    #it will return a 400
    if not request.json or not 'userID' in request.json:
        abort(400)
    locationData = {
        'userID': request.json['userID'],
        'latitude': request.json['latitude'],
        'longitude': request.json['longitude'],
        'timestamp' : request.json['timestamp']
    }
    #tasks.append(task)
    return jsonify({'data': locationData}), 200

@app.route('/')
def hello():
    return "Hello world", 200

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080))
    )