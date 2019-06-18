import sys
sys.path.append('..')
from db import db
from datetime import datetime


class Bookings(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    cust_name = db.Column(db.String(20), unique=True, nullable=False)
    resturant_name = db.Column(db.String(200), nullable=False, default='default.jpg')
    no_of_seats = db.Column(db.String(60), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # resturant_id = db.relationship('resturant', backref='resturant_name', lazy=True)


class Resturant(db.Model):
    __tablename__ = 'resturant'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(20), nullable=False)
    resturant_name = db.Column(db.String(200), nullable=False)
    no_of_seats = db.Column(db.Integer, nullable=False)
