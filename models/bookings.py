from datetime import datetime

from db import db


class Bookings(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cust_name = db.Column(db.String(20), unique=True, nullable=False)
    no_of_seats = db.Column(db.String(60), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref='customer', lazy=True)
    restaurant = db.relationship('Restaurant', backref='restaurant', lazy=True)

    def to_json(self):
        return dict(booking_id=self.id, customer_name=self.cust_name,
                    no_of_seats=self.no_of_seats, customer_details=self.customer.to_json(),
                    restaurant_details=self.restaurant.to_json())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_booking(self):
        db.session.delete(self)
        db.session.commit()

    def all_list(self):
        return dict(booking_id=self.id, customer_name=self.cust_name,
                    no_of_seats=self.no_of_seats,
                    customer_details=dict(cust_name=self.customer.name,
                                          cust_id=self.customer.id,
                                          phone=self.customer.phone,
                                          email=self.customer.email),
                    restaturant_details=dict(restaurant_name=self.restaurant.restaurant_name,
                                             restaturant_phone=self.restaurant.phone))
