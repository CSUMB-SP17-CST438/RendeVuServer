import flask_sqlalchemy, app

#for heroku
app.app.config['SQLALCHEMY_DATABASE_URI'] = app.os.getenv('DATABASE_URL')
# app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://payinvader:girlscoutcookies1@localhost/postgres'

db = flask_sqlalchemy.SQLAlchemy(app.app)


class Users(db.Model):
    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)  # key
    user_id = db.Column(db.String(200))
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    email = db.Column(db.String(200))
    imgUrl = db.Column(db.String(300))
    phoneNumber = db.Column(db.String(20))

    def __init__(self, user_id, firstName, lastName, email, imgUrl, phoneNumber):
        
        self.user_id = user_id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.imgUrl = imgUrl
        self.phoneNumber = phoneNumber

    def __repr__(self):
        return '%s %s %s %s %s %s' % (self.user_id, self.firstName, self.lastName, self.email, self.imgUrl, self.phoneNumber)
        
        
class Location(db.Model):
    __tablename__ = 'location_table'
    
    id = db.Column(db.Integer, primary_key=True)  # key
    userID = db.Column(db.String(200))#requester
    latitude = db.Column(db.Float)#requestee
    longitude = db.Column(db.Float())
    time_stamp = db.Column(db.String(30))
    
    def __init__(self, owed_ID, pay_ID, amount, time_stamp):
    
        self.UserID = owed_ID
        self.userID = userID
        self.latitude = latitude
        self.longitude = longitude
        self.time_stamp = time_stamp
    
    def __repr__(self):
        return '%s %f %f %s' % (self.owed_ID, self.pay_ID, self.amount, self.time_stamp)
        