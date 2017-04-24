import os
import sys
import json
import requests
import flask_sqlalchemy
import time
from flask import Flask, render_template, request, jsonify, abort, make_response

from twilio.rest import Client
app = Flask(__name__)

#for heroku
#app.config['SQLALCHEMY_DATABASE_URI'] = app.os.getenv('DATABASE_URL')
# app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://payinvader:girlscoutcookies1@localhost/postgres'

db = flask_sqlalchemy.SQLAlchemy(app)

# for twilio
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")






# Find these values at https://twilio.com/user/account

client = Client(account_sid, auth_token)

client.messages.create(
    to="+18314285108",
    from_="+15005550006",
    body="This is the ship that made the Kessel Run in fourteen parsecs?",
    media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e")

#import models

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1.0/postInfo', methods=['POST'])
def create_task():
    log("someone pinged the postInfo api")
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
    
    # new_location = models.Location(userData['userID'], 
    #                         userData['latitude'], 
    #                         userData['longitude'], 
    #                         userData['timestamp']
    # )
    # models.db.session.add(new_location)
    # models.db.session.commit()
    # #tasks.append(task)
    return jsonify({'data': locationData}), 200
    
@app.route('/api/v1.0/signup', methods=['POST'])
def signup():
    log("someone pinged signup api")
    log(request.json)
    
    #if the json data does not have the 'usedID' header
    #it will return a 400
    if not request.json or not 'userID' in request.json:
        abort(400)
    userData = {
        'userID': request.json['userID'],
        'firstName': request.json['firstName'],
        'lastName': request.json['lastName'],
        'email': request.json['email'],
        'phoneNumber': request.json['phoneNumber'],
        'timestamp' : request.json['timestamp'],
        'imgURL' : request.json['imgURL'],
    }
    
    # new_user = models.Users(userData['userID'], 
    #                         userData['firstName'], 
    #                         userData['lastName'], 
    #                         userData['email'],
    #                         userData['phoneNumber'],
    #                         userData['timestamp']
    # )
    # models.db.session.add(new_user)
    # models.db.session.commit()
    # #tasks.append(task)
    return jsonify({'data': userData}), 200
    
@app.route('/api/v1.0/login', methods=['POST'])
def login():
    log("someone pinged login the api")
    log(request.json)
    
    #if the json data does not have the 'usedID' header
    #it will return a 400
    if not request.json or not 'userID' in request.json:
        abort(400)
    userData = {
        'userID': request.json['userID'],
    }
    
    user_ids = []
    # message = models.Users.query.with_entities(models.Users.user_id).all()
    
    # for theId in message:
    #     print theId[0]
    #     user_ids.append(str(theId[0]))
    
    # if str(userData['userID']) in user_ids:
    #     userSignedUp = {
    #         'userID': 'true'
    #     }
    # else:
    #     userSignedUp = {
    #         'userID': 'false'
    #     }
    # #tasks.append(task)
    return jsonify({'data': {'userID': 'true'}}), 200

@app.route('/api/v1.0/send', methods=['POST'])
def send():
    log("someone pinged login the api")
    log(request.json)
    
    #if the json data does not have the 'usedID' header
    #it will return a 400
    if not request.json or not 'userID' in request.json:
        abort(400)
    userData = {
        'userID': request.json['userID'],
        'number': request.json['number'],
        'message': request.json['message']
    }
    
    message = userData['message']
    message = "test"
    

    return 200

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