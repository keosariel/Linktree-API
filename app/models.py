from app import db, bcrypt
from flask import current_app

import jwt
from datetime import datetime, timedelta
from hashlib import md5

class User(db.Model):
	
    __tablename__ = 'user'

    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(30), nullable=True)
    username      = db.Column(db.String(20), nullable=False, unique=True)
    email         = db.Column(db.String(256), nullable=False, unique=True)
    password      = db.Column(db.String(256), nullable=False)

    public_id     = db.Column(db.Text, nullable=True, unique=True)
    
    cover_photo   = db.Column(db.Text, nullable=True)
    profile_photo = db.Column(db.Text, nullable=True)
    description   = db.Column(db.Text, nullable=True)
    website       = db.Column(db.Text, nullable=True)

    verified      = db.Column(db.Boolean, default=False)

    deleted       = db.Column(db.Boolean, default=False)

    created_at    = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at   = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    links        = db.relationship('Link', order_by='Link.id', backref='user', lazy=True)
    social_links = db.relationship('SocialLink', order_by='SocialLink.id', backref='user', lazy=True)

    
    def __init__(self, username, email):
        self.username = username        
        self.email = email

    def set_public_id(self):
        """Sets a Public ID for User"""

        self.public_id = get_public_id(f"{self.id}_user")
        self.save()

    def set_password(self, password):
        """Hashes User password"""

        self.password = bcrypt.generate_password_hash(password).decode()
    
    def password_is_valid(self, password):
        """
        Checks the password against it's hash to validates the user's password
        """
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self, user=None):
        """Returns Users data as JSON/Dictionary"""

        _dict = {}
        if not self.deleted:
            links = [ link.to_dict() for link in self.links if not link.deleted ]
            links.reverse()
            social_links = [social_link.to_dict() for social_link in self.social_links]
            _dict = {
                "public_id"     : self.public_id,
                "name"          : self.name,
                "username"      : self.username,
                "email"         : self.email if user == self else None,
                "description"   : self.description,
                "website"       : self.website,
                "verified"      : self.verified,
                "links"         : links,
                "social_links"  : social_links
            }

        return _dict
    
    def delete(self):
        """Deletes User"""

        self.deleted = True
        self.save()
        
    def save(self):
        """Save/Updates the database"""

        db.session.add(self)
        db.session.commit()


    def generate_token(self, minutes=40320):
        """ Generates the access token"""

        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=minutes),
                'iat': datetime.utcnow(),
                'sub': self.id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_string = jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )

            if type(jwt_string) == bytes:
                jwt_string = jwt_string.decode()

            return jwt_string

        except Exception as e:
            # return an error in string format if an exception occurs
            return str(e)

    @staticmethod
    def decode_token(token):
        """Decodes the access token from the Authorization header."""

        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
            return True, payload['sub']
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return False, "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return False, "Invalid token. Please register or login"
        
        return False, "Invalid token. Please register or login"



class Link(db.Model):
    __tablename__ = 'link'

    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(20), nullable=False)
    description   = db.Column(db.Text, nullable=True)
    url           = db.Column(db.Text, nullable=True)
    image         = db.Column(db.Text, nullable=True)
    public_id     = db.Column(db.Text, nullable=True, unique=True)

    deleted     = db.Column(db.Boolean, default=False)

    created_at    = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at   = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    
    user_id       = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __init__(self, title, description, url, user_id, float_value=0.0):

        self.title  = title        
        self.user_id     = user_id
        self.description = description
        self.url         = url
        self.float_value = float_value if float_value else 0.0

    def set_public_id(self):
        """Sets a Public ID for Link"""

        self.public_id = get_public_id(f"{self.id}_link")
        self.save()

    def to_dict(self):
        """Returns Link's data as JSON/Dictionary"""

        _dict = {}
        if not self.deleted:
            _dict = {
                "title"  : self.title,
                "public_id"   : self.public_id,
                "description" : self.description,
                "url"         : self.url
            }

        return _dict

    def delete(self):
        self.deleted = True
        self.save()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
class SocialLink(db.Model):
    __tablename__ = 'social_link'

    id            = db.Column(db.Integer, primary_key=True)
    platform_id   = db.Column(db.Integer, nullable=False)
    url           = db.Column(db.Text, nullable=False)

    user_id       = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    created_at    = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at   = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    deleted     = db.Column(db.Boolean, default=False)

    def __init__(self, platform_id, url, user_id):
        self.url     = url
        self.user_id = user_id    
        self.platform_id = platform_id
    
    def set_public_id(self):
        """Sets a Public ID for SocialLink"""

        self.public_id = get_public_id(f"{self.id}_sociallink")
        self.save()

    def to_dict(self):
        """Returns SocialLink's data as JSON/Dictionary"""

        return {
            "platform_id" : self.platform_id,
            "url" : self.url
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

from app.utils.functions import get_public_id